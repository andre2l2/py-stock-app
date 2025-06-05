from fastapi import FastAPI

from presentation.routes import products

app = FastAPI()

app.include_router(products.router, prefix="/products")
