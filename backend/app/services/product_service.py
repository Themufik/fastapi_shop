from sqlalchemy.orm import Session
from typing import List
from ..repositories.product_repository import ProductRepository
from ..repositories.category_repository import CategoryRepository
from schemas.product import ProductResponse, ProductListResponce, ProductCreate
from fastapi import HTTPException, status



class ProductService:
    def __init__(self, db = Session):
        self.product_repository = ProductRepository(db)
        self.category_repository = CategoryRepository(db)
        
        
    def get_all_products(self) -> List[ProductListResponce]:
        products = self.product_repository.get_all()
        products_response = [ProductResponce.model_validate(prod) for prod in products]
        return ProductListResponse(products = products_response, total = len(products_response))
    
    def get_product_by_id(self, product_id : int) -> ProductListResponse:
        product = self.product_repository.get_bi_id(product_id)
        if not product:
            raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"Produc with id {product_id} not found")
        return ProductRepository.model_validate(product)
    
    def cteate_product(self, product, product_data: ProductCreate) -> ProductRespomse:
        category = self.category_repository.get_by_id(product_data.category_id)
        if not category : 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail= f"Category with id {product_data.category_id} does not exist")
        product = self.product_repository.create(category_data)
        return ProductResponse.model_validate(product) 