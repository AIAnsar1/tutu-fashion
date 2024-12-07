from sqlalchemy import Column, ForeignKey
from backend.app.db import Base
from backend.app.models.basemodel import BaseModel






class ProductImage(BaseModel, Base):

    __tablename__ = "product_images"

    image_id = Column(ForeignKey("images.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)


    @classmethod
    def seed(cls, fake, product_id, image_id):
        product_image = ProductImage(id=fake.uuid4(), product_id=product_id, image_id=image_id)
        return product_image