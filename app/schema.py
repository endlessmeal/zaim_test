from pydantic import BaseModel


class Loan(BaseModel):
    product_name: str

