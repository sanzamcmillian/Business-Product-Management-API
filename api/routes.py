from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.schemas import ProductCreate, ProductResponse
from api.crud import create_product, get_products, get_product_by_id, update_product, delete_product
from storage.database import get_db

router = APIRouter()

# Route for creating a product
@router.post("/v1/products", response_model=ProductResponse)
def create_product_api(product: ProductCreate, db: Session = Depends(get_db)):
    return create_product(db=db, product_data=product)

# Route for getting all products with pagination
@router.get("/v1/products", response_model=list[ProductResponse])
def get_products_api(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_products(db=db, skip=skip, limit=limit)

# Route for getting a product by ID
@router.get("/v1/products/{product_id}", response_model=ProductResponse)
def get_product_by_id_api(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id(db=db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# Route for updating a product
@router.put("/v1/products/{product_id}", response_model=ProductResponse)
def update_product_api(product_id: int, product: ProductCreate, db: Session = Depends(get_db)):
    updated_product = update_product(db=db, product_id=product_id, product_data=product)
    if updated_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

# Route for deleting a product
@router.delete("/v1/products/{product_id}", response_model=ProductResponse)
def delete_product_api(product_id: int, db: Session = Depends(get_db)):
    deleted_product = delete_product(db=db, product_id=product_id)
    if deleted_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return deleted_product
