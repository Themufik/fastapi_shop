from sqlalchemy import Column, Integer, String
from sqalchemy.orm import relationship 
from ..database import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key = True, index = True)
    name = Column(Str, uniqie = True, nullable = False, index = True)
    slug = Column(Str, uniqie = True, nullable = False, index = True)
    
    products  = relationship("Product", back_populates = "category") 
    
    
    def __repr__(self):
        return f"<Category(id={self.id}, name = '{self.name}')"