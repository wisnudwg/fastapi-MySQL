from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import src.config as config

engine = create_engine(config.DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()