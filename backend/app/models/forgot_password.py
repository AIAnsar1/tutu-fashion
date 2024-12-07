from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, text
from backend.app.db import Base
from backend.app.models.basemodel import BaseModel





class ForgotPassword(BaseModel, Base):

    __tablename__ = "forgot_passwords"

    token = Column(String(length=16), nullable=False)
    expires_in = Column(DateTime(timezone=True), nullable=False, server_default=text("now() + interval '15 minutes'"))
    user_id = Column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
















