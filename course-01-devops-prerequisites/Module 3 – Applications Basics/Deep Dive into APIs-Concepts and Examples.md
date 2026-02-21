## **1. What is an API?**
**API** (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other.

### **Key Characteristics:**
- **Contract between services**: Defines how to request data and what response to expect
- **Language-agnostic**: APIs can be consumed by any programming language
- **Stateless**: Each request contains all necessary information (RESTful principle)

## **2. Types of APIs**

### **A. By Architecture/Protocol:**

**1. REST (Representational State Transfer)**
```http
GET /api/users/123
POST /api/users
PUT /api/users/123
DELETE /api/users/123
```

**2. GraphQL** (Query language for APIs)
```graphql
query {
  user(id: "123") {
    name
    email
    posts {
      title
    }
  }
}
```

**3. gRPC** (Google's Remote Procedure Call)
```protobuf
service UserService {
  rpc GetUser(UserRequest) returns (UserResponse);
}
```

**4. SOAP** (Simple Object Access Protocol)
```xml
<soap:Envelope>
  <soap:Body>
    <GetUser>
      <UserId>123</UserId>
    </GetUser>
  </soap:Body>
</soap:Envelope>
```

### **B. By Accessibility:**
- **Public/Open APIs** (Twitter, Google Maps)
- **Partner APIs** (B2B integrations)
- **Internal/Private APIs** (Microservices within company)
- **Composite APIs** (Combine multiple APIs)

## **3. REST API Deep Dive**

### **Core Principles (RESTful constraints):**
1. **Client-Server Architecture**
2. **Statelessness**
3. **Cacheability**
4. **Uniform Interface**
5. **Layered System**
6. **Code on Demand (optional)**

### **HTTP Methods & CRUD Operations:**
| Method | CRUD | Idempotent | Safe | Description |
|--------|------|------------|------|-------------|
| GET | Read | Yes | Yes | Retrieve resource |
| POST | Create | No | No | Create new resource |
| PUT | Update/Replace | Yes | No | Replace entire resource |
| PATCH | Update/Modify | No | No | Partial update |
| DELETE | Delete | Yes | No | Remove resource |
| HEAD | - | Yes | Yes | Get headers only |
| OPTIONS | - | Yes | Yes | Get supported methods |

### **HTTP Status Codes:**
- **2xx Success**: 200 OK, 201 Created, 204 No Content
- **3xx Redirection**: 301 Moved Permanently, 304 Not Modified
- **4xx Client Error**: 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found
- **5xx Server Error**: 500 Internal Server Error, 503 Service Unavailable

## **4. Comprehensive Example: E-commerce API**

### **API Design: Product Management System**

```python
# FastAPI Implementation (Python)
from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import uuid

app = FastAPI(title="E-Commerce API", version="1.0.0")

# ========== MODELS ==========
class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None
    price: float = Field(..., gt=0)
    category: str
    stock_quantity: int = Field(..., ge=0)
    
class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    stock_quantity: Optional[int] = None

class Product(ProductBase):
    id: str
    created_at: datetime
    updated_at: datetime
    is_active: bool = True
    
    class Config:
        from_attributes = True

# ========== DATABASE (Simulated) ==========
class Database:
    def __init__(self):
        self.products = {}
    
    def create_product(self, product_data: dict) -> Product:
        product_id = str(uuid.uuid4())
        now = datetime.utcnow()
        product = Product(
            id=product_id,
            created_at=now,
            updated_at=now,
            **product_data
        )
        self.products[product_id] = product.dict()
        return product
    
    def get_product(self, product_id: str) -> Optional[Product]:
        if product_id in self.products:
            return Product(**self.products[product_id])
        return None
    
    def update_product(self, product_id: str, update_data: dict) -> Optional[Product]:
        if product_id in self.products:
            product_data = self.products[product_id]
            for key, value in update_data.items():
                if value is not None:
                    product_data[key] = value
            product_data['updated_at'] = datetime.utcnow()
            return Product(**product_data)
        return None
    
    def delete_product(self, product_id: str) -> bool:
        if product_id in self.products:
            del self.products[product_id]
            return True
        return False
    
    def list_products(self, skip: int = 0, limit: int = 10) -> List[Product]:
        products = list(self.products.values())[skip:skip + limit]
        return [Product(**p) for p in products]

db = Database()

# ========== DEPENDENCIES ==========
async def get_db():
    return db

# ========== ENDPOINTS ==========

# GET /products - List all products with pagination
@app.get("/products", response_model=List[Product])
async def list_products(
    skip: int = 0,
    limit: int = 10,
    category: Optional[str] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None,
    db: Database = Depends(get_db)
):
    """Retrieve products with filtering and pagination"""
    products = db.list_products(skip, limit)
    
    # Apply filters
    if category:
        products = [p for p in products if p.category == category]
    if min_price is not None:
        products = [p for p in products if p.price >= min_price]
    if max_price is not None:
        products = [p for p in products if p.price <= max_price]
    
    return products

# GET /products/{id} - Get single product
@app.get("/products/{product_id}", response_model=Product)
async def get_product(
    product_id: str,
    db: Database = Depends(get_db)
):
    """Retrieve a specific product by ID"""
    product = db.get_product(product_id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found"
        )
    return product

# POST /products - Create new product
@app.post("/products", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    product: ProductCreate,
    db: Database = Depends(get_db)
):
    """Create a new product"""
    return db.create_product(product.dict())

# PUT /products/{id} - Update entire product
@app.put("/products/{product_id}", response_model=Product)
async def update_product(
    product_id: str,
    product_update: ProductCreate,
    db: Database = Depends(get_db)
):
    """Replace an entire product"""
    existing = db.get_product(product_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return db.update_product(product_id, product_update.dict())

# PATCH /products/{id} - Partial update
@app.patch("/products/{product_id}", response_model=Product)
async def partial_update_product(
    product_id: str,
    product_update: ProductUpdate,
    db: Database = Depends(get_db)
):
    """Partially update a product"""
    existing = db.get_product(product_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Remove None values
    update_data = {k: v for k, v in product_update.dict().items() if v is not None}
    
    return db.update_product(product_id, update_data)

# DELETE /products/{id} - Delete product
@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product_id: str,
    db: Database = Depends(get_db)
):
    """Delete a product"""
    if not db.delete_product(product_id):
        raise HTTPException(status_code=404, detail="Product not found")

# ========== ADVANCED FEATURES ==========

# HEAD endpoint
@app.head("/products/{product_id}")
async def product_head(product_id: str, db: Database = Depends(get_db)):
    """Get headers for a product (useful for checking existence)"""
    product = db.get_product(product_id)
    if not product:
        raise HTTPException(status_code=404)
    return {}

# OPTIONS endpoint
@app.options("/products")
async def products_options():
    """Return allowed methods for /products endpoint"""
    return {"Allow": "GET, POST, HEAD, OPTIONS"}

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "service": "ecommerce-api"
    }

# Batch operations
@app.post("/products/batch")
async def batch_create_products(
    products: List[ProductCreate],
    db: Database = Depends(get_db)
):
    """Create multiple products at once"""
    created_products = []
    for product in products:
        created_products.append(db.create_product(product.dict()))
    return created_products
```

## **5. Client Examples (Consuming the API)**

### **Python Client:**
```python
import requests
import json

class ECommerceClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
    
    # Create product
    def create_product(self, product_data):
        response = self.session.post(
            f"{self.base_url}/products",
            json=product_data
        )
        response.raise_for_status()
        return response.json()
    
    # Get product with error handling
    def get_product(self, product_id):
        try:
            response = self.session.get(
                f"{self.base_url}/products/{product_id}"
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                print(f"Product {product_id} not found")
                return None
            raise
    
    # Update product (partial)
    def update_product(self, product_id, updates):
        response = self.session.patch(
            f"{self.base_url}/products/{product_id}",
            json=updates
        )
        response.raise_for_status()
        return response.json()
    
    # List products with query parameters
    def list_products(self, category=None, min_price=None, max_price=None):
        params = {}
        if category:
            params['category'] = category
        if min_price:
            params['min_price'] = min_price
        if max_price:
            params['max_price'] = max_price
        
        response = self.session.get(
            f"{self.base_url}/products",
            params=params
        )
        response.raise_for_status()
        return response.json()

# Usage
client = ECommerceClient()

# Create a product
new_product = {
    "name": "Wireless Headphones",
    "description": "Noise-cancelling wireless headphones",
    "price": 199.99,
    "category": "Electronics",
    "stock_quantity": 50
}

created = client.create_product(new_product)
print(f"Created product: {created['id']}")

# Get product
product = client.get_product(created['id'])
print(f"Product price: ${product['price']}")

# Update stock
updated = client.update_product(created['id'], {"stock_quantity": 45})
print(f"Updated stock: {updated['stock_quantity']}")

# List electronics products
electronics = client.list_products(category="Electronics")
print(f"Found {len(electronics)} electronics products")
```

### **JavaScript/Node.js Client:**
```javascript
// Using fetch API
class ECommerceAPIClient {
    constructor(baseUrl = 'http://localhost:8000') {
        this.baseUrl = baseUrl;
        this.defaultHeaders = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        };
    }

    async request(endpoint, options = {}) {
        const url = `${this.baseUrl}${endpoint}`;
        const response = await fetch(url, {
            ...options,
            headers: { ...this.defaultHeaders, ...options.headers }
        });

        if (!response.ok) {
            const error = await response.json().catch(() => ({}));
            throw new Error(`API Error ${response.status}: ${error.detail || response.statusText}`);
        }

        // For 204 No Content responses
        if (response.status === 204) {
            return null;
        }

        return await response.json();
    }

    // Create product
    async createProduct(productData) {
        return this.request('/products', {
            method: 'POST',
            body: JSON.stringify(productData)
        });
    }

    // Get product with caching headers
    async getProduct(productId, useCache = true) {
        const headers = useCache ? {} : { 'Cache-Control': 'no-cache' };
        return this.request(`/products/${productId}`, { headers });
    }

    // Batch operations
    async batchCreateProducts(products) {
        return this.request('/products/batch', {
            method: 'POST',
            body: JSON.stringify(products)
        });
    }
}

// Usage with async/await
async function main() {
    const client = new ECommerceAPIClient();
    
    try {
        // Health check
        const health = await client.request('/health');
        console.log('Service status:', health.status);
        
        // Create multiple products
        const products = [
            {
                name: "Laptop",
                price: 999.99,
                category: "Electronics",
                stock_quantity: 10
            },
            {
                name: "Desk Chair",
                price: 149.99,
                category: "Furniture",
                stock_quantity: 25
            }
        ];
        
        const created = await client.batchCreateProducts(products);
        console.log(`Created ${created.length} products`);
        
    } catch (error) {
        console.error('API Error:', error.message);
    }
}

main();
```

### **cURL Examples:**
```bash
# 1. Create a product
curl -X POST http://localhost:8000/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Smartphone",
    "price": 699.99,
    "category": "Electronics",
    "stock_quantity": 100
  }'

# 2. Get a product
curl http://localhost:8000/products/{product_id}

# 3. Update product (partial)
curl -X PATCH http://localhost:8000/products/{product_id} \
  -H "Content-Type: application/json" \
  -d '{"price": 649.99}'

# 4. Delete a product
curl -X DELETE http://localhost:8000/products/{product_id}

# 5. List with filters
curl "http://localhost:8000/products?category=Electronics&min_price=500"

# 6. Check headers only
curl -I http://localhost:8000/products/{product_id}

# 7. Health check
curl http://localhost:8000/health
```

## **6. Advanced API Concepts**

### **A. Authentication & Authorization:**
```python
# JWT Authentication example
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt

security = HTTPBearer()

@app.post("/secure/products")
async def create_secure_product(
    product: ProductCreate,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Database = Depends(get_db)
):
    # Verify JWT token
    token = credentials.credentials
    try:
        payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
        user_id = payload.get("sub")
        # Check user permissions...
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    return db.create_product(product.dict())
```

### **B. Rate Limiting:**
```python
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.get("/products")
@limiter.limit("10/minute")
async def list_products(request: Request, db: Database = Depends(get_db)):
    return db.list_products()
```

### **C. WebSocket API (Real-time updates):**
```python
from fastapi import WebSocket

@app.websocket("/ws/products/{product_id}")
async def websocket_product_updates(websocket: WebSocket, product_id: str):
    await websocket.accept()
    try:
        while True:
            # Wait for messages from client
            data = await websocket.receive_json()
            
            # Send real-time updates
            product = db.get_product(product_id)
            await websocket.send_json({
                "type": "update",
                "product": product.dict() if product else None
            })
    except WebSocketDisconnect:
        print("Client disconnected")
```

### **D. Webhook Implementation:**
```python
@app.post("/webhooks/product-updated")
async def product_webhook(payload: dict):
    """
    Example webhook payload:
    {
        "event": "product.updated",
        "data": {"product_id": "123", "changes": {"price": 199.99}},
        "timestamp": "2024-01-15T10:30:00Z"
    }
    """
    event_type = payload.get("event")
    
    if event_type == "product.updated":
        product_id = payload["data"]["product_id"]
        # Notify subscribers, update cache, etc.
        print(f"Product {product_id} was updated")
    
    return {"status": "webhook received"}
```

## **7. API Testing Examples**

### **Pytest Tests:**
```python
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_product():
    """Test product creation"""
    response = client.post("/products", json={
        "name": "Test Product",
        "price": 99.99,
        "category": "Test",
        "stock_quantity": 10
    })
    
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Product"
    assert "id" in data

def test_get_nonexistent_product():
    """Test 404 for non-existent product"""
    response = client.get("/products/nonexistent")
    assert response.status_code == 404

def test_update_product():
    """Test product update"""
    # First create
    create_response = client.post("/products", json={
        "name": "Update Test",
        "price": 50,
        "category": "Test",
        "stock_quantity": 5
    })
    product_id = create_response.json()["id"]
    
    # Then update
    update_response = client.patch(
        f"/products/{product_id}",
        json={"price": 55}
    )
    assert update_response.status_code == 200
    assert update_response.json()["price"] == 55

def test_rate_limiting():
    """Test rate limiting"""
    for _ in range(11):  # Exceed 10/minute limit
        response = client.get("/products")
    assert response.status_code == 429  # Too Many Requests
```

## **8. API Documentation (OpenAPI/Swagger)**

FastAPI automatically generates documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`
- **OpenAPI JSON**: `http://localhost:8000/openapi.json`

### **Customizing Documentation:**
```python
@app.post(
    "/products",
    response_model=Product,
    status_code=201,
    summary="Create a new product",
    description="""
    Create a new product in the e-commerce system.
    
    **Requirements:**
    - Product name must be 1-100 characters
    - Price must be greater than 0
    - Stock quantity cannot be negative
    """,
    responses={
        201: {"description": "Product created successfully"},
        400: {"description": "Invalid input data"},
        401: {"description": "Not authenticated"}
    },
    tags=["Products"]
)
async def create_product(product: ProductCreate):
    return db.create_product(product.dict())
```

## **9. Best Practices**

### **Design Principles:**
1. **Use nouns, not verbs** in endpoints: `/products` not `/getProducts`
2. **Version your API**: `/api/v1/products`
3. **Use plural nouns for collections**: `/products`, `/users`
4. **Nested resources for relationships**: `/products/{id}/reviews`
5. **Filter, sort, paginate**: `/products?category=electronics&sort=price&page=2`
6. **Return appropriate HTTP status codes**
7. **Provide meaningful error messages**
8. **Use consistent casing (recommend snake_case for JSON)**
9. **Implement HATEOAS for discoverability** (optional)

### **Performance Tips:**
1. **Implement pagination** for list endpoints
2. **Use caching headers** (ETag, Last-Modified)
3. **Compress responses** (gzip)
4. **Implement rate limiting**
5. **Use connection pooling**
6. **Monitor API metrics** (response times, error rates)

### **Security Considerations:**
1. **Always use HTTPS** in production
2. **Validate all inputs**
3. **Implement proper authentication/authorization**
4. **Sanitize output data**
5. **Set CORS policies appropriately**
6. **Use API keys for external consumers**
7. **Implement request signing** for critical operations

## **10. Monitoring & Observability**

```python
# Adding logging and metrics
import logging
from prometheus_client import Counter, Histogram

# Metrics
REQUEST_COUNT = Counter('api_requests_total', 'Total API requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('api_request_duration_seconds', 'API request latency', ['endpoint'])

# Middleware for monitoring
@app.middleware("http")
async def monitor_requests(request: Request, call_next):
    start_time = time.time()
    
    response = await call_next(request)
    
    duration = time.time() - start_time
    REQUEST_LATENCY.labels(endpoint=request.url.path).observe(duration)
    REQUEST_COUNT.labels(
        method=request.method,
        endpoint=request.url.path,
        status=response.status_code
    ).inc()
    
    return response
```

## **Conclusion**

This deep dive covered:
1. **API fundamentals** and types
2. **REST API design** with complete implementation
3. **Client examples** in multiple languages
4. **Advanced features** like authentication, WebSockets, webhooks
5. **Testing strategies**
6. **Documentation** and **best practices**
7. **Monitoring** and **observability**

APIs are the backbone of modern software architecture. A well-designed API follows REST principles, provides clear documentation, handles errors gracefully, and includes proper security measures. The example e-commerce API demonstrates how to implement these concepts in practice.

Remember: The best APIs are **consistent**, **intuitive**, **well-documented**, and **reliable**.