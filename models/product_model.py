from pydantic import BaseModel
from typing import List, Optional

class ProductModel(BaseModel):
    name: str
    description: str
    sizes: List[str]
    price: float
