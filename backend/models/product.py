from sqlalchemy import Column, Integer, String, Float
from .base import Base

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    price = Column(Float, default=0.0)
