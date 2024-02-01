from sqlalchemy import Boolean, Column, Integer, String

from src.models import Base

class Post(Base):
  __tablename__ = "posts"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String(50))
  content = Column(String(100))
  user_id = Column(Integer)