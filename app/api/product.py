from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.product import Product
from app.schemas.product import ProductCreate
from app.schemas.product import ProductUpdate

router = APIRouter()

@router.post("/products")
def create_product(product: ProductCreate):
    db = SessionLocal()

    new_product = Product(
        name=product.name,
        price=product.price,
        quantity=product.quantity
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return new_product

@router.get("/products")
def list_products():
    db = SessionLocal()
    
    products = db.query(Product).all()
    
    return products

@router.get("/products/{product_id}")
def get_product(product_id: int):
    db = SessionLocal()

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return {"error": "Produto não encontrado"}

    return product

@router.put("/products/{product_id}")
def update_product(product_id: int, product_data: ProductUpdate):
    db = SessionLocal()

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return {"error": "Produto não encontrado"}

    product.name = product_data.name
    product.price = product_data.price
    product.quantity = product_data.quantity

    db.commit()
    db.refresh(product)

    return product

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    db = SessionLocal()

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return {"error": "Produto não encontrado"}

    db.delete(product)
    db.commit()

    return {"message": "Produto deletado com sucesso"}