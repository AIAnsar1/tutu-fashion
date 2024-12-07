from sqlalchemy import Column, String, Index
from backend.app.db import Base
from backend.app.models.basemodel import BaseModel




class Image(BaseModel, Base):

    __tablename__ = "images"

    name = Column(String(length=128), nullable=False, unique=True)
    image_url = Column(String(length=128), nullable=False, unique=True)

    __table_args__ = (Index("image_url", image_url), { "extend_existing": True })


    @classmethod
    def seed(cls, fake, name, url):
        image = Image(id=fake.uuid4(), name=name, image_url=url)
        return image