# TOML Tutorial: A Technical Guide for Developers

> **TOML** stands for _Tom's Obvious, Minimal Language_, created by Tom Preston-Werner (co-founder of GitHub). It is a configuration file format designed to be easy to read due to obvious semantics, and unambiguous to parse into a hash table/dictionary.

**Official spec:** [https://toml.io](https://toml.io/) **Current stable version:** TOML 1.0.0

---

## Table of Contents

1. [Why TOML?](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#why-toml)
2. [File Conventions](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#file-conventions)
3. [Comments](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#comments)
4. [Key-Value Pairs](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#key-value-pairs)
5. [Keys: Bare, Quoted, Dotted](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#keys-bare-quoted-dotted)
6. [Strings](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#strings)
7. [Integers](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#integers)
8. [Floats](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#floats)
9. [Booleans](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#booleans)
10. [Date and Time](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#date-and-time)
11. [Arrays](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#arrays)
12. [Tables](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#tables)
13. [Inline Tables](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#inline-tables)
14. [Arrays of Tables](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#arrays-of-tables)
15. [Real-World Examples](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#real-world-examples)
16. [Parsing TOML in Different Languages](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#parsing-toml-in-different-languages)
17. [Common Pitfalls](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#common-pitfalls)
18. [TOML vs. JSON vs. YAML](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#toml-vs-json-vs-yaml)
19. [Best Practices](https://claude.ai/chat/75f56471-87a9-407a-970b-3c751362b26a#best-practices)

---

## Why TOML?

TOML aims to be a **minimal configuration file format** that's easy to read due to obvious semantics. It was designed to map unambiguously to a hash table.

**Strengths:**

- Human-readable with minimal syntax overhead
- Strongly typed (strings, integers, floats, booleans, dates, arrays, tables)
- Unambiguous parsing — no whitespace-sensitivity gotchas like YAML
- Native support for comments (unlike JSON)
- Excellent for static configuration files

**Common use cases:**

- `Cargo.toml` (Rust package manager)
- `pyproject.toml` (Python PEP 518/621 standard)
- `.cargo/config.toml`, `rustfmt.toml`
- Hugo static site generator config
- `poetry.lock`, `uv.lock` (Python lockfiles)

---

## File Conventions

- **Extension:** `.toml`
- **MIME type:** `application/toml`
- **Encoding:** UTF-8 (required)
- **Line endings:** LF (`\n`) or CRLF (`\r\n`)
- **Whitespace:** Tab (`0x09`) or Space (`0x20`)
- **Case-sensitive:** Yes — `Name` and `name` are different keys

---

## Comments

A hash symbol (`#`) marks the rest of the line as a comment, except when inside a string.

```toml
# This is a full-line comment
key = "value"  # This is an inline comment

# Multi-line comments don't exist — use multiple # lines instead
# Line 1
# Line 2
```

Control characters other than tab are **not permitted** in comments.

---

## Key-Value Pairs

The primary building block of a TOML document. Each pair appears on its own line.

```toml
key = "value"
```

**Rules:**

- The key is on the left of the `=` sign
- The value is on the right
- Whitespace around `=` is ignored
- Keys may not be empty (`= "no key"` is invalid)
- Values **must** be specified — `key =` without a value is invalid
- Each key/value pair must be on its own line (newline-terminated)

```toml
# Valid
first = "Tom"
last = "Preston-Werner"

# Invalid — no value
key =

# Invalid — two pairs on one line
first = "Tom" last = "Preston-Werner"
```

---

## Keys: Bare, Quoted, Dotted

TOML supports three key styles.

### Bare Keys

May contain only ASCII letters, digits, underscores, and dashes: `A-Za-z0-9_-`

```toml
key = "value"
bare_key = "value"
bare-key = "value"
1234 = "value"  # All digits is allowed
```

### Quoted Keys

Follow the exact same rules as basic or literal strings — allows any Unicode character.

```toml
"127.0.0.1" = "localhost"
"character encoding" = "value"
"ʎǝʞ" = "value"
'quoted "value"' = "value"
```

### Dotted Keys

Express hierarchy by separating with dots. Whitespace around dots is ignored.

```toml
physical.color = "orange"
physical.shape = "round"
site."google.com" = true
```

Equivalent JSON representation:

```json
{
  "physical": { "color": "orange", "shape": "round" },
  "site": { "google.com": true }
}
```

**Important:** Defining a key more than once is invalid.

```toml
# INVALID
name = "Tom"
name = "Pradyun"

# INVALID — implicit redefinition
fruit.apple = 1
fruit.apple.smooth = true  # error: apple was already a value
```

---

## Strings

TOML has four ways to express strings.

### 1. Basic Strings

Surrounded by quotation marks (`"`). Support escape sequences.

```toml
str = "I'm a string. \"You can quote me\". Name\tJos\u00E9\nLocation\tSF."
```

**Supported escape sequences:**

|Escape|Meaning|
|---|---|
|`\b`|Backspace (U+0008)|
|`\t`|Tab (U+0009)|
|`\n`|Linefeed (U+000A)|
|`\f`|Form feed (U+000C)|
|`\r`|Carriage return (U+000D)|
|`\"`|Quote (U+0022)|
|`\\`|Backslash (U+005C)|
|`\uXXXX`|Unicode (4 hex digits)|
|`\UXXXXXXXX`|Unicode (8 hex digits)|

### 2. Multi-line Basic Strings

Surrounded by three quotation marks (`"""`). Newlines preserved.

```toml
str1 = """
Roses are red
Violets are blue"""

# A backslash at the end of a line trims all whitespace until the next non-whitespace char
str2 = """\
       The quick brown \
       fox jumps over \
       the lazy dog.\
       """
# str2 == "The quick brown fox jumps over the lazy dog."
```

### 3. Literal Strings

Surrounded by single quotes (`'`). **No escaping** — what you see is what you get. Useful for Windows paths or regex.

```toml
winpath  = 'C:\Users\nodejs\templates'
winpath2 = '\\ServerX\admin$\system32\'
quoted   = 'Tom "Dubs" Preston-Werner'
regex    = '<\i\c*\s*>'
```

### 4. Multi-line Literal Strings

Surrounded by three single quotes (`'''`). No escaping at all.

```toml
regex2 = '''I [dw]on't need \d{2} apples'''

lines  = '''
The first newline is
trimmed in raw strings.
   All other whitespace
   is preserved.
'''
```

---

## Integers

Whole numbers. May be prefixed with a plus or minus. Underscores allowed between digits for readability (not at the start, end, or adjacent to another underscore).

```toml
int1 = +99
int2 = 42
int3 = 0
int4 = -17

# Underscores for readability
int5 = 1_000
int6 = 5_349_221
int7 = 53_49_221       # Indian numbering system
int8 = 1_2_3_4_5       # Valid but discouraged

# Non-decimal integers (with prefixes)
hex1 = 0xDEADBEEF
hex2 = 0xdeadbeef
hex3 = 0xdead_beef
oct1 = 0o01234567      # Octal
oct2 = 0o755           # Useful for Unix permissions
bin1 = 0b11010110      # Binary
```

**Range:** 64-bit signed long range, i.e., −9,223,372,036,854,775,808 to 9,223,372,036,854,775,807.

---

## Floats

IEEE 754 binary64 values.

```toml
# Fractional
flt1 = +1.0
flt2 = 3.1415
flt3 = -0.01

# Exponent
flt4 = 5e+22
flt5 = 1e06
flt6 = -2E-2

# Both
flt7 = 6.626e-34

# Underscores allowed
flt8 = 224_617.445_991_228

# Special values
sf1 = inf   # Positive infinity
sf2 = +inf
sf3 = -inf
sf4 = nan   # Not a Number
sf5 = +nan
sf6 = -nan
```

**Note:** A float consists of an integer part followed by a fractional part, an exponent part, or both. If both are used, the fractional part must precede the exponent.

---

## Booleans

Always lowercase.

```toml
bool1 = true
bool2 = false
```

---

## Date and Time

TOML has first-class support for dates and times — a major advantage over JSON.

### Offset Date-Time

Combined date and time with timezone offset (RFC 3339).

```toml
odt1 = 1979-05-27T07:32:00Z
odt2 = 1979-05-27T00:32:00-07:00
odt3 = 1979-05-27T00:32:00.999999-07:00
odt4 = 1979-05-27 07:32:00Z   # Space separator also allowed
```

### Local Date-Time

No timezone — represents a wall-clock time.

```toml
ldt1 = 1979-05-27T07:32:00
ldt2 = 1979-05-27T00:32:00.999999
```

### Local Date

Date with no time, no offset.

```toml
ld1 = 1979-05-27
```

### Local Time

Time with no date, no offset.

```toml
lt1 = 07:32:00
lt2 = 00:32:00.999999
```

---

## Arrays

Square brackets with values separated by commas. Arrays may contain mixed types in TOML 1.0.

```toml
integers = [ 1, 2, 3 ]
colors   = [ "red", "yellow", "green" ]
nested_arrays_of_ints = [ [ 1, 2 ], [3, 4, 5] ]
nested_mixed_array    = [ [ 1, 2 ], ["a", "b", "c"] ]
string_array          = [ "all", 'strings', """are the same""", '''type''' ]

# Mixed-type arrays are allowed (TOML 1.0+)
numbers = [ 0.1, 0.2, 0.5, 1, 5 ]
contributors = [
  "Foo Bar <foo@example.com>",
  { name = "Baz Qux", email = "bazqux@example.com", url = "https://example.com" }
]

# Arrays may span multiple lines, trailing commas allowed
integers2 = [
  1, 2, 3,
]

integers3 = [
  1,
  2,    # comments allowed
  3,
]
```

---

## Tables

Tables (a.k.a. hash tables, dictionaries) are defined with a header in square brackets on a line by itself.

```toml
[table]
key1 = "some string"
key2 = 123
```

Under that header, until the next header or EOF, are the key/values of that table.

### Nested Tables with Dotted Headers

```toml
[dog."tater.man"]
type.name = "pug"
```

Equivalent JSON:

```json
{
  "dog": {
    "tater.man": {
      "type": { "name": "pug" }
    }
  }
}
```

### Whitespace in Dotted Headers

Whitespace around dot-separated parts is ignored, but best practice is no extra whitespace.

```toml
[a.b.c]            # Preferred
[ d.e.f ]          # Same as [d.e.f]
[ g .  h  . i ]    # Same as [g.h.i]
[ j . "ʞ" . 'l' ]  # Same as [j."ʞ".'l']
```

### Order Doesn't Matter (Mostly)

Sub-tables can appear before their parents in the file, but it's strongly discouraged stylistically.

```toml
# VALID but ugly
[x.y.z.w]

[x]
```

### Tables Without Headers

The "root table" begins at the start of the document and ends before the first table header (or EOF).

```toml
# Belongs to the root table
title = "TOML Example"

[owner]
name = "Tom Preston-Werner"
```

### Defining a Table Twice Is an Error

```toml
# INVALID
[fruit]
apple = "red"

[fruit]   # error
orange = "orange"
```

---

## Inline Tables

A more compact syntax for expressing tables. Use curly braces with comma-separated key/value pairs. **No newlines allowed inside.**

```toml
name = { first = "Tom", last = "Preston-Werner" }
point = { x = 1, y = 2 }
animal = { type.name = "pug" }
```

Equivalent to:

```toml
[name]
first = "Tom"
last = "Preston-Werner"

[point]
x = 1
y = 2

[animal]
type.name = "pug"
```

Inline tables are **self-contained** — you cannot add or change keys after definition.

```toml
[product]
type = { name = "Nail" }
# type.edible = false   # INVALID
```

---

## Arrays of Tables

The last syntax that hasn't been described allows writing arrays of tables. Double-bracket headers (`[[...]]`).

```toml
[[products]]
name = "Hammer"
sku = 738594937

[[products]]   # empty table within the array

[[products]]
name = "Nail"
sku = 284758393
color = "gray"
```

Equivalent JSON:

```json
{
  "products": [
    { "name": "Hammer", "sku": 738594937 },
    { },
    { "name": "Nail", "sku": 284758393, "color": "gray" }
  ]
}
```

### Nested Arrays of Tables

```toml
[[fruits]]
name = "apple"

[fruits.physical]  # subtable
color = "red"
shape = "round"

[[fruits.varieties]]  # nested array of tables
name = "red delicious"

[[fruits.varieties]]
name = "granny smith"

[[fruits]]
name = "banana"

[[fruits.varieties]]
name = "plantain"
```

Equivalent JSON:

```json
{
  "fruits": [
    {
      "name": "apple",
      "physical": { "color": "red", "shape": "round" },
      "varieties": [
        { "name": "red delicious" },
        { "name": "granny smith" }
      ]
    },
    {
      "name": "banana",
      "varieties": [ { "name": "plantain" } ]
    }
  ]
}
```

---

## Real-World Examples

### Example 1: `Cargo.toml` (Rust)

```toml
[package]
name = "my-crate"
version = "0.1.0"
edition = "2021"
authors = ["Jane Doe <jane@example.com>"]
license = "MIT OR Apache-2.0"
description = "A high-quality crate doing useful things"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1.35", features = ["full"] }
anyhow = "1.0"

[dev-dependencies]
criterion = "0.5"

[[bench]]
name = "my_benchmark"
harness = false

[profile.release]
opt-level = 3
lto = true
codegen-units = 1
```

### Example 2: `pyproject.toml` (Python PEP 621)

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "my-package"
version = "0.1.0"
description = "Sample Python package"
readme = "README.md"
requires-python = ">=3.10"
authors = [
  { name = "Jane Doe", email = "jane@example.com" },
]
dependencies = [
  "requests>=2.31",
  "pydantic>=2.0",
]

[project.optional-dependencies]
dev = ["pytest>=7.0", "ruff>=0.1", "mypy>=1.0"]

[project.scripts]
my-cli = "my_package.cli:main"

[tool.ruff]
line-length = 100
target-version = "py310"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### Example 3: A Server Config

```toml
title = "Server Config"

[server]
host = "0.0.0.0"
port = 8080
workers = 4
read_timeout = "30s"
tls.enabled = true
tls.cert = "/etc/ssl/server.crt"
tls.key  = "/etc/ssl/server.key"

[database]
url = "postgres://user:pass@localhost/mydb"
pool_size = 20
connect_timeout = 5

[[database.replicas]]
host = "replica1.example.com"
port = 5432

[[database.replicas]]
host = "replica2.example.com"
port = 5432

[logging]
level = "info"
format = "json"
outputs = ["stdout", "/var/log/app.log"]
```

---

## Parsing TOML in Different Languages

### Python (3.11+)

```python
# Read (stdlib, Python 3.11+)
import tomllib

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

# Write (third-party — tomllib doesn't write)
import tomli_w
with open("out.toml", "wb") as f:
    tomli_w.dump(config, f)
```

For Python < 3.11, use `tomli` (read) and `tomli-w` (write).

### Rust

```rust
use serde::Deserialize;

#[derive(Deserialize)]
struct Config {
    server: Server,
}

#[derive(Deserialize)]
struct Server {
    host: String,
    port: u16,
}

let s = std::fs::read_to_string("config.toml")?;
let config: Config = toml::from_str(&s)?;
```

`Cargo.toml` dependency:

```toml
toml = "0.8"
serde = { version = "1.0", features = ["derive"] }
```

### Go

```go
import "github.com/BurntSushi/toml"

type Config struct {
    Server struct {
        Host string
        Port int
    }
}

var cfg Config
_, err := toml.DecodeFile("config.toml", &cfg)
```

### Node.js / JavaScript

```javascript
import { parse, stringify } from "smol-toml";  // or @iarna/toml

const text = await Deno.readTextFile("config.toml");
const data = parse(text);
const back = stringify(data);
```

### Java

Use `tomlj/tomlj` or `Mojang/Brigadier`:

```java
TomlParseResult result = Toml.parse(Paths.get("config.toml"));
String host = result.getString("server.host");
```

---

## Common Pitfalls

### 1. Defining a Key Twice

```toml
# INVALID
spelling = "favorite"
"spelling" = "favourite"   # Quoted/bare resolve to same key
```

### 2. Defining a Table After a Subtable

```toml
[fruit.apple]
smooth = true

[fruit]   # error — fruit was already defined implicitly
```

**Fix:** Define parents first.

```toml
[fruit]

[fruit.apple]
smooth = true
```

### 3. Mixing a Table and an Array-of-Tables with the Same Name

```toml
# INVALID
[[fruit]]
name = "apple"

[fruit]   # error — already an array-of-tables
```

### 4. Adding to an Inline Table After Definition

```toml
# INVALID
point = { x = 1, y = 2 }
point.z = 3   # error
```

### 5. Newlines Inside Inline Tables

```toml
# INVALID — inline tables must be on one line
point = {
  x = 1,
  y = 2
}
```

### 6. Leading Zeros in Integers

```toml
# INVALID
flight = 0042
```

Use a string if you need leading zeros: `flight = "0042"`.

### 7. Trailing Commas in Inline Tables

```toml
# INVALID — trailing commas not allowed in inline tables
point = { x = 1, y = 2, }

# VALID — trailing commas OK in arrays
items = [ 1, 2, 3, ]
```

---

## TOML vs. JSON vs. YAML

|Feature|TOML|JSON|YAML|
|---|---|---|---|
|Comments|✅|❌|✅|
|Trailing commas|Arrays only|❌|N/A|
|Native dates|✅|❌|✅|
|Whitespace-sensitive|❌|❌|✅|
|Multi-line strings|✅|❌ (must escape)|✅|
|Strongly typed|✅|✅|✅|
|Anchors/refs|❌|❌|✅|
|Schema-friendly|✅|✅|⚠️|
|Ambiguity risk|Low|Low|High ("Norway problem", `yes` → `true`)|
|Spec complexity|Low|Very low|High|

**Rule of thumb:**

- **TOML** — configuration files written by humans
- **JSON** — data interchange between machines / web APIs
- **YAML** — complex hierarchical configs (Kubernetes, Ansible) where anchors and references matter

---

## Best Practices

1. **Group related settings under tables** rather than using long dotted keys at the root.
2. **Prefer explicit `[table]` headers** over deeply dotted keys in mixed contexts — easier to read.
3. **Use literal strings (`'...'`) for paths and regex** to avoid escape-character pain on Windows.
4. **Always define parent tables before child tables** in source order, even though TOML doesn't strictly require it.
5. **Don't mix types in arrays unless necessary** — even though TOML 1.0 permits it, it complicates downstream parsing.
6. **Use snake_case for keys** by convention in most communities (Rust, Python).
7. **Pin TOML versions** for critical configs — TOML 0.5 vs. 1.0 differ in subtle ways (array type homogeneity, key uniqueness rules).
8. **Validate against a schema** where possible (e.g., `taplo`, `validator` crate in Rust).
9. **Prefer inline tables for small, self-contained values** (a coordinate, a single dependency spec); use full table headers for sections with many keys.
10. **Comment why, not what** — TOML's self-describing nature means you rarely need to explain _what_ a key does; explain rationale or non-obvious constraints.

---

## Further Reading

- [Official TOML Specification](https://toml.io/en/v1.0.0)
- [TOML on GitHub](https://github.com/toml-lang/toml)
- [Awesome TOML — curated list of tools, parsers, validators](https://github.com/toml-lang/awesome-toml)
- [`taplo`](https://taplo.tamasfe.dev/) — TOML language server, formatter, and validator
- [TOML Playground](https://www.toml-lint.com/) — online validator

---

_This document covers TOML 1.0.0. Earlier versions (0.4, 0.5) have minor syntactic and semantic differences — consult the spec history if you're working with legacy parsers._