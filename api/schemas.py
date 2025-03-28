from pydantic import BaseModel
from enum import Enum
from typing import Optional


class StockStatus(str, Enum):
    in_stock = "in_stock"
    out_of_stock = "out_of_stock"
    pre_order = "pre_order"


class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    category: str
    price: float
    stock_status: StockStatus = StockStatus.in_stock
    sku: str


class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True