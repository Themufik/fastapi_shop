from pydantic import BaseModel, Field
from datetime import datetime 
from typing import Optional


class CartItemBase(BaseModel):
    product_id : str = Field(..., description="Product Id")
    quantity : str = Field(..., gt=0, description= "Quantity (must be greater than 0)")
    
    
class CartItemCreate(CartItemBase):
    pass


class CatrItemUpdate(BaseModel):
    product_id : int = Field(..., description="Product ID")
    quanity : int = Field(..., gt=0, description="New quanity (must greater than 0)")
    
    
    
class CartItem(BaseModel):
    product_id : int
    name : str = Field(...,)
    price : float = Field(..., description="Product price")
    quanity : int = Field(..., "Product quanity") 
    subtotal : float = Field(..., description="Total price for this item (price * quanity) ")
    image_irt : Optional[str] = Field(None, description="Product image URL")
    