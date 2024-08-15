# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    email: str

users_db = []

@app.post("/users/", response_model=User)
async def create_user(user: User):
    for existing_user in users_db:
        if existing_user.email == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    users_db.append(user)
    return user
