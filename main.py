from fastapi import FastAPI
from routes import products, orders

app = FastAPI()

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
@app.get("/")
def read_root():
    return {"message": "Ecommerce backend is up and running 🚀"}
