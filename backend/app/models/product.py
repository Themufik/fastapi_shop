from sqlalchemy import Column, Integer, String, Text, Float, DatatTime, ForeginKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, index = True)
    name = Column(String, unique= False, nullable= False, index=True)
    description = Column(Text)
    price = Column(Float, nullable= False)
    category_id = Column(Integer, ForeginKey("categories.id"), nullable=False)
    image_url = Column(String)
    created_at = Column(DatatTime, default=datetime.utcnow)
    
    
def __repr__():
    return f"<Product(id = {self.id}, name = '{self.name}', price  = {self.price})>"
    