from fastapi import APIRouter, Query
from models.product_model import ProductModel
from db import products_collection
from bson import ObjectId
from fastapi.responses import JSONResponse
import re

router = APIRouter()

@router.post("")
def create_product(product: ProductModel):
    result = products_collection.insert_one(product.dict())
    return JSONResponse(status_code=201, content={"message": "Product created", "id": str(result.inserted_id)})

@router.get("")
def list_products(name: str = None, size: str = None, limit: int = 10, offset: int = 0):
    filters = {}
    if name:
        filters["name"] = {"$regex": name, "$options": "i"}
    if size:
        filters["sizes"] = size

    cursor = products_collection.find(filters).skip(offset).limit(limit)
    products = []
    for product in cursor:
        product["_id"] = str(product["_id"])
        products.append(product)
    return products
