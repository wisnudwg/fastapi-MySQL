from fastapi import APIRouter, Depends, HTTPException, Response, status
from sqlalchemy import func
from sqlalchemy.orm import Session
from typing import List, Optional

from src.models.post import Post as PostModel
from src.routers import db_dependency
from src.schemas.post import PostBase

router = APIRouter(
  prefix="/posts",
  tags=["Posts"],
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_posts(db: db_dependency):
  db_posts = db.query(PostModel).all()
  return db_posts

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_post(post: PostBase, db: db_dependency):
  db_post = PostModel(**post.dict())
  db.add(db_post)
  db.commit()

@router.post("/{post_id}", status_code=status.HTTP_200_OK)
async def read_post(post_id: int, db: db_dependency):
  db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
  if db_post is None:
    raise HTTPException(status_code=400, detail="post not found")
  return db_post

@router.delete("/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: int, db: db_dependency):
  db_post = db.query(PostModel).filter(PostModel.id == post_id).first()
  if db_post is None:
    raise HTTPException(status_code=400, detail="post not found")
  db.delete(db_post)
  db.commit()