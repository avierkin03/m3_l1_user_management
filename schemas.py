from pydantic import BaseModel


# Схема користувача для Pydantic
class UserCreate(BaseModel):
    username: str
    email: str