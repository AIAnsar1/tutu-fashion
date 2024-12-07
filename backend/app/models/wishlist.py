from sqlalchemy import Column, ForeignKey, UniqueConstraint
from backend.app.db import Base
from backend.app.models.basemodel import BaseModel




class Wishlist(Base, BaseModel):

    __tablename__ = "wishlists"

    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    product_id = Column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)

    __table_args__ = (UniqueConstraint("user_id", "product_id"),)



    @classmethod
    def seed(cls, fake, user_id, product_id):
        wishlist = Wishlist(id=fake.uuid4(), user_id=user_id, product_id=product_id)
        return wishlist










