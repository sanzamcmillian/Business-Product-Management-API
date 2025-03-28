from alembic.operations.toimpl import create_constraint
from sqlalchemy import Column, Integer, String, Float, Enum
from .database import Base
import enum


class Stockstatus(enum.Enum):
    in_stock = "in_stock"
    out_of_stock = "out_of_stock"
    pre_order = "pre_order"


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    stock_status = Column(Enum(Stockstatus, names="stock_status"), nullable=False, default=Stockstatus.in_stock)
    sku = Column(String, unique=True, nullable=False)