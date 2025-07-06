# app/schemas.py
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    # İleride parola vb. eklenirse burada tanımlanır
    pass

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
