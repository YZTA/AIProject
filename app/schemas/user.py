import uuid
from pydantic import BaseModel, EmailStr

# Kullanıcı veritabanından okunurken kullanılacak temel şema
class UserBase(BaseModel):
    email: EmailStr

# Yeni bir kullanıcı oluşturulurken alınacak veri
class UserCreate(UserBase):
    password: str

# API'den bir kullanıcı döndürülürken kullanılacak şema
# (hash'lenmiş şifreyi dışarı sızdırmaz)
class UserPublic(UserBase):
    id: uuid.UUID
    is_active: bool

    class Config:
        from_attributes = True