import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID
import uuid
from app.db import Base, db_engine


class Products(Base):
    __tablename__ = "products"
    UUID = sa.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    product_name = sa.Column(sa.String())

    @classmethod
    async def create_loan(
            cls,
            *,
            product_name: str
    ) -> "Products":
        query = cls.insert_query(
            product_name=product_name
        )

        async with db_engine.client.acquire() as conn:
            cursor = await conn.execute(query)
            return await cursor.fetchone()

    @classmethod
    async def get_loan_by_id(
            cls,
            *,
            product_uuid: UUID,
    ) -> "Products":
        query = cls.select_query().where(Products.UUID == product_uuid)

        async with db_engine.client.acquire() as conn:
            cursor = await conn.execute(query)
            return await cursor.fetchone()
