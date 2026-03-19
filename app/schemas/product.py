from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    quantity: int

class ProductUpdate(BaseModel):
    name: str
    price: float
    quantity: int