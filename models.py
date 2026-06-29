class Product:
    id:int
    name:str
    description:str
    price:float

    def __init__(self, id, name, description, price):
        self.id = id
        self.name = name
        self.description = description
        self.price = price