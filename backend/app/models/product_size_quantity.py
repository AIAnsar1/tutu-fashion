from sqlalchemy import Column, Integer, ForeignKey
from backend.app.db import Base
from backend.app.models.basemodel import BaseModel




class ProductSizeQuantity(Base, BaseModel):

    __tablename__ = "product_size_quantities"

    quantity = Column(Integer, nullable=False)
    product_id = Column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    size_id = Column(ForeignKey("sizes.id", ondelete="CASCADE"), nullable=False)


    @classmethod
    def seed(cls, fake, product_id, size_id):
        product_size_quantity = ProductSizeQuantity(id=fake.uuid4(), quantity=fake.pyint(min_value=1000), product_id=product_id, size_id=size_id)
        return product_size_quantity