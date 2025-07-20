from fastapi import APIRouter
from db import orders_collection, products_collection
from models.order_model import OrderModel
from bson import ObjectId
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("")
def create_order(order: OrderModel):
    result = orders_collection.insert_one({"product_ids": [ObjectId(pid) for pid in order.product_ids]})
    return JSONResponse(status_code=201, content={"message": "Order created", "id": str(result.inserted_id)})

@router.get("")
def list_orders():
    pipeline = [
        {
            "$lookup": {
                "from": "products",
                "localField": "product_ids",
                "foreignField": "_id",
                "as": "products"
            }
        }
    ]
    orders = list(orders_collection.aggregate(pipeline))
    for order in orders:
        order["_id"] = str(order["_id"])
        for product in order["products"]:
            product["_id"] = str(product["_id"])
    return orders
