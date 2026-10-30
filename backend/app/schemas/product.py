from pydantic import BaseModel, Field
from datetime import datetime 
from typing import Optional
from .category import CategoryResponse


class ProductBase(BaseModel):
    name : str = Field(..., min_length=5, max_length=200, description = "Product name")
    description : Optional[str] = Field(None, description = "Product Description")
    price : float = Field(..., gt=0, description='Product price must be greater than 0')
    
    category_id : int = Field(..., description="Category ID")
    
    image_irl : Optional[str] = Field(None, description="Product image irl")
    
    
class ProductCreate(ProductBase):
    pass
    
    
class ProductResponse(BaseModel):
    id : int = Field(..., description='Uniaue product ID')
    name : str 
    description : Optional[str]
    price : float
    
    category_id: int
    
    image_url : Optional[str]
    created_at : datetime
    category : CategoryResponse = Field(..., description="Product caregory details")
    
    class Config:
        from_attributes = True 
        
class ProductListResponse(BaseModel):
    products : list[ProductResponse]
    total : int = Field(..., description="Total number of products")
    
    
    
