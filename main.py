from fastapi import FastAPI, HTTPException
from models import Product

app = FastAPI()
@app.get("/")
def greet():
    return "Welcome to Telusko"

products = [
    Product(1,"laptop","high performance laptop",1000),
    Product(2,"mouse","high performance mouse",100),
    Product(3,"keyboard","high performance keyboard",100),
    Product(4,"monitor","high performance monitor",100),
    Product(5,"webcam","high performance webcam",100),
]
@app.get("/products")
def get_all_products():
    return products
@app.get("/products/{id}")
def get_product(id:int):
    for product in products:
        if product.id==id:
            return product
    return "product not found"
    

    
    

