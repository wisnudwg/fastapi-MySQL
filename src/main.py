from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers import post, user

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
async def root():
  return {"data": "fastapi-mySQL"}