from sqlalchemy.orm import Session
from storage.models import Product
from api.schemas import ProductCreate, StockStatus

# Create a new product
def create_product(db: Session, product_data: ProductCreate):
    new_product = Product(**product_data.model_dump())  # Convert Pydantic model to dict
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

# Get all products with pagination
def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Product).offset(skip).limit(limit).all()

# Get a product by ID
def get_product_by_id(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

# Update a product
def update_product(db: Session, product_id: int, product_data: ProductCreate):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None
    for key, value in product_data.model_dump().items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product

# Delete a product
def delete_product(db: Session, product_id: int):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        return None
    db.delete(product)
    db.commit()
    return product
