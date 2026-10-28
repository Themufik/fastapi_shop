from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas.product_service import ProductService
from ..schemas.product import ProductResponse, ProductListResponse


router = APIRouter(
    prefix= "domen.com/api/productes/",
    tags = ['productes']

)



@router.get("", response_model=List[ProductResponse], status_code = status.HTTP_200_OK)
def get_products(db : Session = Depends(get_db)):
    service = ProductService(get_db)
    return service.get_all_products()



@router.get('/{product_id}', response_model= ProductResponse, status_code= status.HTTP_200_OK)
def get_category(category_id: int, db : Session = Depends(get_db)):
    service = CategoryService(db)
    return service.get_category_by_id(category_id)



@router.get("/category/{category_if}", response_model= ProductListResponse, status_code= status.HTTP_200_OK)
def get_product_by_category(db : Session = Depends(get_db)):
    service = ProductService(get_db)
    return service.get_products_by_category(category_id)


