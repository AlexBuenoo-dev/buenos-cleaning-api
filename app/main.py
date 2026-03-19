from fastapi import FastAPI
from app.db.session import engine, Base
from app.models import product
from app.api import product
from app.api import sale


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(product.router)

app.include_router(sale.router)

@app.get("/")
def read_root():
    return {"message": "API Buenos Cleaning funcionando 🚀"}

