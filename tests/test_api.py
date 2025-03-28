import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)  # Create a test client

# Test 1: Create a Product
def test_create_product():
    response = client.post("/v1/products/", json={
        "name": "Test Product",
        "description": "This is a test product",
        "category": "Electronics",
        "price": 49.99,
        "stock_status": "in_stock",
        "sku": "rES123"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Product"

# Test 2: Fetch All Products
def test_get_products():
    response = client.get("/v1/products/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test 3: Fetch Single Product (Adjust ID Based on Your DB)
def test_get_single_product():
    response = client.get("/v1/products/1")  # Assuming a product exists with ID=1
    assert response.status_code == 200
    assert "name" in response.json()

# Test 4: Update Product
def test_update_product():
    response = client.put("/v1/products/1", json={
        "name": "Updated Product",
        "description": "Updated description",
        "category": "Electronics",
        "price": 79.99,  # Updating price
        "stock_status": "in_stock",
        "sku": "UPDATED123"
    })
    assert response.status_code == 200
    assert response.json()["price"] == 79.99

# Test 5: Delete Product
def test_delete_product():
    response = client.delete("/v1/products/1")
    assert response.status_code == 204  # No content after deletion
