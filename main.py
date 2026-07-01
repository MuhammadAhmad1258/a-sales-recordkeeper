from fastapi import FastAPI, HTTPException
from models import Product
from database import session,Base,engine
app = FastAPI()
@app.get("/")
def greet():
    return "Welcome to Telusko"

products = [
    Product(id=1, name="laptop", description="high performance laptop", price=1000),
    Product(id=2, name="mouse", description="high performance mouse", price=100),
    Product(id=3, name="keyboard", description="high performance keyboard", price=100),
    Product(id=4, name="monitor", description="high performance monitor", price=100),
    Product(id=5, name="webcam", description="high performance webcam", price=100),
]
@app.get("/products")
def get_all_products():
    db = session()
    products = db.query(Product).all()
    return products
@app.get("/products/{id}")
def get_product(id:int):
    for product in products:
        if product.id==id:
            return product
    return "product not found"
@app.post("/products")


def add_product(product: Product):
    for p in products:
        if p.id == product.id:
            raise HTTPException(status_code=400, detail="Product with this id already exists")
    products.append(product)
    return product
@app.delete("/products/{id}")
def delete_product(id:int):
    for product in products:
        if product.id==id:
            products.remove(product)
            return "product deleted"
    return "product not found"
@app.put("/products/{id}")
def update_product(id:int,product:Product):
    for p in products:
        if p.id==id:
            p.name=product.name
            p.description=product.description
            p.price=product.price
            return "product updated"
    return "product not found"
    
    
