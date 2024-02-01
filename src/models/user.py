from sqlalchemy import Boolean, Column, Integer, String

from src.models import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String(50), unique=True)