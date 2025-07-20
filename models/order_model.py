from pydantic import BaseModel
from typing import List

class OrderModel(BaseModel):
    product_ids: List[str]
