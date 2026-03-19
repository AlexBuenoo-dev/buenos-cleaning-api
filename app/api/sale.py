from fastapi import APIRouter
from app.db.session import SessionLocal
from app.models.product import Product
from app.schemas.sale import SaleCreate

router = APIRouter()

@router.post("/sales")
def create_sale(sale: SaleCreate):
    db = SessionLocal()

    product = db.query(Product).filter(Product.id == sale.product_id).first()

    if not product:
        return {"error": "Produto não encontrado"}

    if product.quantity < sale.quantity:
        return {"error": "Estoque insuficiente"}

    product.quantity -= sale.quantity

    db.commit()

    return {
        "message": "Venda realizada com sucesso",
        "product_id": product.id,
        "remaining_stock": product.quantity
    }