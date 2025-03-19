from sqlalchemy import Column, Integer, String
from database import Base


# Модель користувача
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String, index = True)
    email = Column(String, index = True)