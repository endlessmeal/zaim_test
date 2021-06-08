from fastapi import APIRouter
from app.schema import Loan
from app.models import Products

routes = APIRouter()


@routes.post("/api/v1/loans")
async def create_loan(loan: Loan):
    product = await Products.create_loan(product_name=loan.product_name)
    return {"loan_id": product}


@routes.get("/api/v1/loans/{product_uuid}")
async def get_loan(product_uuid):
    product = await Products.get_loan_by_id(product_uuid=product_uuid)
    return product
