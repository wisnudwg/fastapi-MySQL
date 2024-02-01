from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List, Optional

from src.models.user import User as UserModel
from src.routers import db_dependency
from src.schemas.user import UserBase

router = APIRouter(
  prefix="/users",
  tags=["Users"],
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_users(db: db_dependency):
  db_users = db.query(UserModel).all()
  return db_users

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_users(user: UserBase, db: db_dependency):
  db_user = UserModel(**user.dict())
  db.add(db_user)
  db.commit()

@router.get("/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db: db_dependency):
  user = db.query(UserModel).filter(UserModel.id == user_id).first()
  if user is None:
    raise HTTPException(status_code=404, detail="user not found")
  return user