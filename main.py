from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import UserCreate
from database import SessionLocal, engine
from crud import create_user, get_user, get_all_users
import models


app = FastAPI()


models.Base.metadata.create_all(bind = engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# повертає інформацію про користувача за його ідентифікатором
@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


# повертає список всіх користувачів
@app.get("/users")
def read_all_users(db: Session = Depends(get_db)):
    return get_all_users(db)


# дозволяє створити нового користувача за допомогою POST-запиту
@app.post("/create_user")
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)
