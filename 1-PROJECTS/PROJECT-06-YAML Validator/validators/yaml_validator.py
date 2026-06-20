import yaml
import json
import re
from typing import Dict, List, Tuple, Any, Optional, Union
from dataclasses import dataclass
from enum import Enum
import traceback

class ValidationLevel(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"

@dataclass
class ValidationIssue:
    """Represents a validation issue"""
    level: ValidationLevel
    message: str
    line: Optional[int] = None
    column: Optional[int] = None
    context: Optional[str] = None
    rule_id: Optional[str] = None
    fix: Optional[str] = None

class YAMLValidator:
    """Comprehensive YAML validator"""
    
    # Common YAML pitfalls to check for
    COMMON_ISSUES = {
        'ambiguous_bool': ['on', 'off', 'yes', 'no', 'true', 'false', 'True', 'False', 'YES', 'NO', 'ON', 'OFF'],
        'octal_numbers': r'^0[0-7]+$',
        'leading_zeros': r'^0\d+$',
        'special_chars': r'[^\x00-\x7F]',  # Non-ASCII
        'tab_indentation': r'^\t+',
        'trailing_spaces': r'\s+$',
        'duplicate_keys': None,  # Checked separately
    }
    
    def __init__(self, strict: bool = False, check_common_issues: bool = True):
        self.strict = strict
        self.check_common_issues = check_common_issues
        self.issues: List[ValidationIssue] = []
    
    def validate(self, content: str, filename: str = None) -> Tuple[bool, List[ValidationIssue], Optional[Dict]]:
        """
        Validate YAML content
        
        Args:
            content: YAML content as string
            filename: Optional filename for context
            
        Returns:
            Tuple of (is_valid, issues, parsed_data)
        """
        self.issues = []
        parsed_data = None
        
        # Check for empty content
        if not content.strip():
            self.issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                message="Empty YAML content"
            ))
            return False, self.issues, None
        
        # Try to parse YAML
        try:
            parsed_data = yaml.safe_load(content)
        except yaml.YAMLError as e:
            issue = self._parse_yaml_error(e, content)
            self.issues.append(issue)
            return False, self.issues, None
        
        # Additional checks if parsing succeeded
        if parsed_data is not None:
            # Check for common issues
            if self.check_common_issues:
                self._check_common_issues(content, filename)
            
            # Check for duplicate keys (PyYAML silently overwrites)
            self._check_duplicate_keys(content)
            
            # Check for tabs
            self._check_tab_indentation(content)
            
            # Validate structure if needed
            if self.strict:
                self._validate_structure(parsed_data)
        
        # Check if any errors were found
        has_errors = any(issue.level == ValidationLevel.ERROR for issue in self.issues)
        
        return not has_errors, self.issues, parsed_data
    
    def _parse_yaml_error(self, error: yaml.YAMLError, content: str) -> ValidationIssue:
        """Parse YAML error into ValidationIssue"""
        if hasattr(error, 'problem_mark'):
            mark = error.problem_mark
            line = mark.line + 1 if mark else None
            column = mark.column + 1 if mark else None
            
            # Extract context line
            context = None
            if line and column:
                lines = content.split('\n')
                if 0 <= line - 1 < len(lines):
                    context = lines[line - 1]
                    # Add indicator for column
                    if 0 <= column - 1 <= len(context):
                        indicator = ' ' * (column - 1) + '^'
                        context = f"{context}\n{indicator}"
            
            # Clean up error message
            message = str(error).split(' in ')[0]
            message = message.replace('while parsing a ', '').replace('expected ', '')
            
            return ValidationIssue(
                level=ValidationLevel.ERROR,
                message=f"YAML parsing error: {message}",
                line=line,
                column=column,
                context=context,
                rule_id="yaml-syntax-error"
            )
        
        return ValidationIssue(
            level=ValidationLevel.ERROR,
            message=f"YAML parsing error: {str(error)}",
            rule_id="yaml-syntax-error"
        )
    
    def _check_common_issues(self, content: str, filename: str = None):
        """Check for common YAML pitfalls"""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, start=1):
            # Skip comments and empty lines
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            
            # Check for ambiguous boolean-like strings without quotes
            for ambiguous in self.COMMON_ISSUES['ambiguous_bool']:
                pattern = rf'\b{ambiguous}\b(?=\s*:|$)'
                if re.search(pattern, line) and '"' not in line and "'" not in line:
                    self.issues.append(ValidationIssue(
                        level=ValidationLevel.WARNING,
                        message=f"Ambiguous value '{ambiguous}' should be quoted to avoid boolean interpretation",
                        line=i,
                        column=line.find(ambiguous) + 1 if ambiguous in line else None,
                        context=line,
                        rule_id="ambiguous-value",
                        fix=f'"{ambiguous}"'
                    ))
            
            # Check for octal numbers
            match = re.search(r':\s*(\d+)\s*$', line)
            if match:
                value = match.group(1)
                if re.match(self.COMMON_ISSUES['octal_numbers'], value):
                    self.issues.append(ValidationIssue(
                        level=ValidationLevel.WARNING,
                        message=f"Number '{value}' may be interpreted as octal. Use string or 0o prefix.",
                        line=i,
                        column=line.find(value) + 1,
                        context=line,
                        rule_id="octal-number",
                        fix=f'"{value}"'
                    ))
            
            # Check for trailing spaces
            if re.search(self.COMMON_ISSUES['trailing_spaces'], line):
                self.issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    message="Trailing spaces found",
                    line=i,
                    column=len(line.rstrip()) + 1,
                    context=line,
                    rule_id="trailing-spaces"
                ))
    
    def _check_duplicate_keys(self, content: str):
        """Check for duplicate YAML keys in the same document"""
        lines = content.split('\n')
        in_mapping = []
        mapping_stack = [{}]
        line_stack = [[]]
        
        for i, line in enumerate(lines, start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            
            # Calculate indentation
            indent = len(line) - len(line.lstrip())
            
            # Check if we're exiting a mapping
            while in_mapping and indent <= in_mapping[-1][0]:
                in_mapping.pop()
                mapping_stack.pop()
                line_stack.pop()
            
            # Check for key
            if ':' in line and not line.strip().startswith('-'):
                key_part = line.split(':', 1)[0].strip()
                if key_part and not key_part.startswith('#'):
                    current_level = len(in_mapping)
                    
                    # Check for duplicate at this level
                    if key_part in mapping_stack[-1]:
                        prev_line = line_stack[-1][key_part]
                        self.issues.append(ValidationIssue(
                            level=ValidationLevel.ERROR,
                            message=f"Duplicate key '{key_part}'",
                            line=i,
                            column=line.find(key_part) + 1,
                            context=f"Previous occurrence at line {prev_line}",
                            rule_id="duplicate-key"
                        ))
                    else:
                        mapping_stack[-1][key_part] = True
                        line_stack[-1][key_part] = i
                    
                    # Enter new mapping
                    in_mapping.append((indent, key_part))
                    mapping_stack.append({})
                    line_stack.append({})
    
    def _check_tab_indentation(self, content: str):
        """Check for tab characters in indentation"""
        lines = content.split('\n')
        
        for i, line in enumerate(lines, start=1):
            if re.match(self.COMMON_ISSUES['tab_indentation'], line):
                self.issues.append(ValidationIssue(
                    level=ValidationLevel.ERROR,
                    message="Tab character used for indentation (use spaces instead)",
                    line=i,
                    column=1,
                    context=line[:50],
                    rule_id="tab-indentation"
                ))
    
    def _validate_structure(self, data: Any):
        """Perform additional structural validation"""
        if isinstance(data, dict):
            self._validate_dict(data)
        elif isinstance(data, list):
            self._validate_list(data)
    
    def _validate_dict(self, data: Dict):
        """Validate dictionary structure"""
        for key, value in data.items():
            if not isinstance(key, (str, int, float)):
                self.issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    message=f"Unusual key type: {type(key).__name__}",
                    rule_id="unusual-key-type"
                ))
            self._validate_structure(value)
    
    def _validate_list(self, data: List):
        """Validate list structure"""
        for item in data:
            self._validate_structure(item)
    
    def validate_file(self, filepath: str) -> Tuple[bool, List[ValidationIssue], Optional[Dict]]:
        """Validate YAML file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            return self.validate(content, filepath)
        except (IOError, OSError) as e:
            self.issues.append(ValidationIssue(
                level=ValidationLevel.ERROR,
                message=f"File error: {str(e)}"
            ))
            return False, self.issues, None
    
    def format_as_json(self, data: Dict) -> str:
        """Convert YAML to formatted JSON for comparison"""
        return json.dumps(data, indent=2, ensure_ascii=False)

class YAMLLinter:
    """YAML linter with style checks"""
    
    def __init__(self):
        self.rules = {
            'indentation': {
                'description': 'Use 2 spaces for indentation',
                'severity': 'warning'
            },
            'trailing_spaces': {
                'description': 'No trailing spaces',
                'severity': 'warning'
            },
            'quoted_strings': {
                'description': 'Strings with special characters should be quoted',
                'severity': 'info'
            },
            'line_length': {
                'description': 'Lines should not exceed 80 characters',
                'severity': 'info',
                'max_length': 80
            }
        }
    
    def lint(self, content: str) -> List[ValidationIssue]:
        """Lint YAML content for style issues"""
        issues = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines, start=1):
            # Check line length
            if len(line) > self.rules['line_length']['max_length']:
                issues.append(ValidationIssue(
                    level=ValidationLevel.INFO,
                    message=f"Line exceeds {self.rules['line_length']['max_length']} characters",
                    line=i,
                    rule_id="line-length"
                ))
            
            # Check indentation (should be multiples of 2)
            indent = len(line) - len(line.lstrip())
            if indent % 2 != 0 and indent > 0 and not line.startswith('#'):
                issues.append(ValidationIssue(
                    level=ValidationLevel.WARNING,
                    message="Indentation should be multiples of 2 spaces",
                    line=i,
                    rule_id="indentation"
                ))
        
        return issues