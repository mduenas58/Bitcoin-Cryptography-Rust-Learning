
## **What is YAML?**
**YAML** (YAML Ain't Markup Language, originally "Yet Another Markup Language") is a human-readable data serialization language that's commonly used for configuration files, data exchange, and defining structured data.

## **Core Philosophy**
```yaml
# YAML prioritizes:
- Human readability over machine efficiency
- Clean, minimal syntax
- Logical structure using indentation
- Native data types without extra syntax
```

## **Basic Syntax Rules**

### **1. Indentation Matters!**
```yaml
# CORRECT: 2-space indentation (common)
database:
  host: localhost
  port: 5432
  
# WRONG: Mixed indentation
database:
    host: localhost
  port: 5432  # Error: inconsistent indentation

# Tabs are NOT allowed in YAML
# Use spaces only
```

### **2. Key-Value Pairs**
```yaml
# Simple key-value
name: John Doe
age: 30
active: true

# Multiline strings
description: |
  This is a multiline
  string that preserves
  line breaks and indentation.

# Folded style (single line)
summary: >
  This is a folded string
  that converts newlines
  to spaces for readability.
```

### **3. Comments**
```yaml
# This is a single-line comment
key: value  # Inline comment

# Multiple lines of comments
# Each line needs its own hash

# Note: No block comment syntax exists
```

## **Data Types in YAML**

### **1. Scalars (Single Values)**
```yaml
# Strings (quotes optional)
string1: Hello World
string2: 'Single quotes'
string3: "Double quotes"
string4: 123  # Auto-detected as string if quoted

# Numbers
integer: 42
float: 3.14
scientific: 1.23e+4
infinity: .inf  # Represents infinity
not_a_number: .nan

# Booleans
true_values: 
  - true
  - True
  - TRUE
  - yes
  - Yes
  - YES
  - on
  - On
  - ON

false_values:
  - false
  - False
  - FALSE
  - no
  - No
  - NO
  - off
  - Off
  - OFF

# Null
null_value: null
empty:  # Also represents null
another_null: ~  # Alternative null syntax

# Dates and Times
iso_date: 2024-01-28
datetime: 2024-01-28T14:30:00Z
datetime_with_tz: 2024-01-28T14:30:00-05:00
```

### **2. Collections**
```yaml
# Sequences (Arrays/Lists)
fruits:
  - Apple
  - Banana
  - Cherry

# Inline array
colors: [red, green, blue]

# Nested arrays
matrix:
  - [1, 2, 3]
  - [4, 5, 6]
  - [7, 8, 9]

# Mappings (Objects/Dictionaries)
person:
  name: Alice
  age: 30
  address:
    street: 123 Main St
    city: Boston

# Inline object
car: {make: Toyota, model: Camry, year: 2022}

# Complex nested structure
company:
  name: Tech Corp
  employees:
    - id: 1
      name: John
      skills: [Python, Docker, AWS]
    - id: 2
      name: Jane
      skills: [React, Node.js]
  departments:
    engineering:
      lead: John
      count: 50
    sales:
      lead: Sarah
      count: 20
```

## **Advanced YAML Features**

### **1. Anchors & Aliases (Reusability)**
```yaml
# Define once, reuse multiple times
defaults: &default_settings
  adapter: postgresql
  host: localhost
  port: 5432

development:
  <<: *default_settings  # Merge anchor
  database: dev_db

test:
  <<: *default_settings
  database: test_db

production:
  <<: *default_settings
  host: prod-server.com
  database: prod_db

# Multiple anchors
base_config: &base
  timeout: 30
  retries: 3

extended_config: &extended
  <<: *base
  cache: true
  ttl: 3600

# Nested anchors
server_defaults: &server
  host: localhost
  ports: &ports
    http: 80
    https: 443

server1:
  <<: *server
  name: web1

server2:
  <<: *server
  name: web2
  ports:
    <<: *ports
    custom: 8080
```

### **2. Multi-documents in Single File**
```yaml
# Document 1
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  key: value
...

# Document 2
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app-deployment
spec:
  replicas: 3
...

# Three dashes (---) separate documents
# Three dots (...) optionally end documents
```

### **3. Complex Strings with Block Styles**
```yaml
# Literal Block Scalar (preserves newlines)
code_snippet: |
  function hello() {
    console.log("Hello");
    return true;
  }
  # This comment is preserved
  const x = 10;

# Folded Block Scalar (folds newlines)
paragraph: >
  This is a long paragraph
  that will be folded into
  a single line with spaces
  replacing newlines.
  
  Blank lines become newlines.

# Block styles with indentation indicators
indented_code: |2
    function test() {
      return "indented";
    }
  # The 2 means "remove 2 spaces from each line"

# Chomping indicators
trimmed: |-  # Remove trailing newlines
  No newline at end

keep_newline: |+  # Keep all newlines
  Keeps all
  
  newlines

```

### **4. Tags (Explicit Types)**
```yaml
# Built-in tags
not_a_string: !!str 123  # Forces string type
not_a_number: !!int "456"  # Forces integer
binary_data: !!binary |
  R0lGODlhDAAMAIQAAP//9/X
  17unp5WZmZgAAAOfn515eXv
  Pz7Y6OjuDg4J+fn5OTk6enp
  56enmleECcgggoBADs=
  
# Custom tags
my_object: !CustomType
  property: value
  another: true

# Python-specific (in PyYAML)
python_object: !!python/object:__main__.MyClass
  attr1: value1
  attr2: value2
```

### **5. Flow vs Block Styles**
```yaml
# Block style (default, human-readable)
block_example:
  name: John
  items:
    - item1
    - item2
  nested:
    key: value

# Flow style (JSON-like, compact)
flow_example: {name: John, items: [item1, item2], nested: {key: value}}

# Mixed styles
mixed:
  simple_values: [1, 2, 3]
  complex_structure:
    - {x: 1, y: 2}
    - {x: 3, y: 4}
```

## **YAML in Different Ecosystems**

### **1. Kubernetes Manifests**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
    tier: frontend
spec:
  containers:
  - name: myapp-container
    image: myapp:1.0
    ports:
    - containerPort: 80
    env:
    - name: ENVIRONMENT
      value: "production"
    - name: DATABASE_URL
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: connection-string
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

### **2. GitHub Actions Workflow**
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [14.x, 16.x, 18.x]
    steps:
    - uses: actions/checkout@v3
    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v3
      with:
        node-version: ${{ matrix.node-version }}
    - run: npm ci
    - run: npm test
    - run: npm run build
```

### **3. Docker Compose**
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./app:/code
      - static_volume:/static
    environment:
      - DEBUG=1
      - DATABASE_URL=postgres://postgres@db/postgres
    depends_on:
      - db
      - redis

  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD_FILE=/run/secrets/db_password
    secrets:
      - db_password

  redis:
    image: redis:7-alpine

volumes:
  static_volume:
  postgres_data:

secrets:
  db_password:
    file: ./db_password.txt
```

### **4. Ansible Playbooks**
```yaml
---
- name: Configure web servers
  hosts: webservers
  become: yes
  vars:
    http_port: 80
    max_clients: 200
  
  tasks:
  - name: Ensure nginx is installed
    apt:
      name: nginx
      state: present
      update_cache: yes
    notify: restart nginx
  
  - name: Copy nginx config
    template:
      src: templates/nginx.conf.j2
      dest: /etc/nginx/sites-available/default
    notify: restart nginx
  
  handlers:
  - name: restart nginx
    service:
      name: nginx
      state: restarted
```

## **Common Pitfalls & Best Practices**

### **Pitfalls to Avoid:**
```yaml
# 1. Inconsistent indentation
bad:           # 2 spaces
    nested:    # 4 spaces - ERROR!
      value: 1

# 2. Ambiguous booleans
danger: off    # String or boolean?
safe: "off"    # Explicitly string

# 3. Octal numbers
permissions: 0777  # Parsed as decimal 777
safer: "0777"      # String or use 0o777

# 4. Special characters without quotes
unicode: café      # Might cause issues
safe_unicode: "café"  # Safer

# 5. Leading zeros
zip_code: 00123    # Parsed as octal 83!
correct_zip: "00123"  # String

# 6. YAML injection (!!python/object)
dangerous: !!python/object:os.system
  args: ["rm -rf /"]  # NEVER load untrusted YAML!
```

### **Best Practices:**
```yaml
# 1. Use consistent 2-space indentation
consistent:
  level1:
    level2:
      level3: value

# 2. Quote strings when ambiguous
always_quote:
  - "true"      # String, not boolean
  - "123"       # String, not number
  - "2024-01-28"  # String, not date
  - "null"      # String, not null
  - "café"      # Special characters
  - "0777"      # Leading zeros

# 3. Use explicit typing when needed
explicit_types:
  string_number: !!str 42
  actual_number: 42
  string_boolean: !!str true
  actual_boolean: true

# 4. Use anchors for DRY configuration
common: &common_settings
  timeout: 30
  retry: 3

service_a:
  <<: *common_settings
  name: service-a

service_b:
  <<: *common_settings
  name: service-b

# 5. Validate your YAML
# Use: yamllint, yq, or online validators
```

## **YAML Processing Tools**

### **Command Line Tools:**
```bash
# yq (jq for YAML)
yq eval '.key.subkey' file.yaml
yq eval -i '.image.tag = "v2.0"' deploy.yaml

# yamllint
yamllint file.yaml

# Convert YAML to JSON
python -c "import yaml,json,sys; print(json.dumps(yaml.safe_load(sys.stdin)))" < file.yaml

# Convert JSON to YAML
python -c "import yaml,json,sys; print(yaml.dump(json.load(sys.stdin)))" < file.json
```

### **Programming Language Libraries:**
```python
# Python (PyYAML)
import yaml

# Safe load (recommended)
data = yaml.safe_load("""
key: value
list:
  - item1
  - item2
""")

# Dump with formatting
yaml.dump(data, default_flow_style=False, indent=2)

# Load with custom constructor
def construct_custom(loader, node):
    return f"Custom: {node.value}"

yaml.add_constructor('!Custom', construct_custom)
```

```javascript
// JavaScript (js-yaml)
const yaml = require('js-yaml');

const doc = yaml.load(`
  key: value
  list:
    - item1
    - item2
`);

const yamlStr = yaml.dump(doc, { indent: 2 });
```

## **Advanced Examples**

### **Complex Configuration:**
```yaml
# Application configuration with multiple environments
application:
  name: "MyApp"
  version: "2.1.0"
  environments:
    development: &dev
      database:
        host: "localhost"
        port: 5432
        name: "dev_db"
      logging:
        level: "DEBUG"
        file: "/tmp/app.log"
      features:
        enabled:
          - "debug_toolbar"
          - "hot_reload"

    staging:
      <<: *dev
      database:
        host: "staging-db.example.com"
        name: "staging_db"
      logging:
        level: "INFO"
      features:
        enabled:
          - "debug_toolbar"

    production:
      database:
        host: "prod-db.example.com"
        port: 5432
        name: "prod_db"
        pool:
          min: 5
          max: 20
          idle_timeout: 30000
      logging:
        level: "WARN"
        targets:
          - type: "file"
            path: "/var/log/app.log"
          - type: "sentry"
            dsn: "https://abc123@sentry.io/1"
      features:
        enabled: []
        flags:
          new_ui: 0.1  # 10% rollout
          api_v2: 0.5  # 50% rollout

# Reusable templates
templates:
  api_endpoint: &api_base
    auth: true
    rate_limit: 1000
    timeout: 30

endpoints:
  users:
    <<: *api_base
    path: "/api/v1/users"
    methods: [GET, POST]

  orders:
    <<: *api_base
    path: "/api/v1/orders"
    methods: [GET, POST, PUT, DELETE]
    rate_limit: 500  # Override
```

### **Multi-lingual Content:**
```yaml
translations:
  welcome:
    en: "Welcome to our application"
    es: "Bienvenido a nuestra aplicación"
    fr: "Bienvenue dans notre application"
    ja: "アプリケーションへようこそ"
  
  buttons:
    submit:
      en: "Submit"
      es: "Enviar"
      fr: "Soumettre"
    
    cancel:
      en: "Cancel"
      es: "Cancelar"
      fr: "Annuler"
```

## **Security Considerations**

### **Never Do This:**
```yaml
# UNSAFE: Loading untrusted YAML with full loader
import yaml
with open('untrusted.yaml') as f:
    data = yaml.load(f)  # DANGER: Executes arbitrary code!

# SAFE: Use safe_load
with open('untrusted.yaml') as f:
    data = yaml.safe_load(f)  # Only loads basic types
```

### **YAML Bomb (Billion Laughs Attack):**
```yaml
# Malicious YAML that can crash parsers
a: &a ["lol","lol","lol","lol","lol","lol","lol","lol","lol"]
b: &b [*a,*a,*a,*a,*a,*a,*a,*a,*a]
c: &c [*b,*b,*b,*b,*b,*b,*b,*b,*b]
d: &d [*c,*c,*c,*c,*c,*c,*c,*c,*c]
e: &e [*d,*d,*d,*d,*d,*d,*d,*d,*d]
f: &f [*e,*e,*e,*e,*e,*e,*e,*e,*e]
g: &g [*f,*f,*f,*f,*f,*f,*f,*f,*f]
h: &h [*g,*g,*g,*g,*g,*g,*g,*g,*g]
i: &i [*h,*h,*h,*h,*h,*h,*h,*h,*h]
```

**Always:**
1. Use `safe_load` or equivalent
2. Validate schemas
3. Set size limits on parsers
4. Keep parsers updated

YAML's power comes from its simplicity and flexibility, but this also requires understanding its nuances and potential pitfalls. When used correctly, it's an excellent format for configuration and data serialization.