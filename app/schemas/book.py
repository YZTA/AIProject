import uuid
from pydantic import BaseModel, HttpUrl
from typing import Optional

# Kitap oluştururken alınacak veri
class BookCreate(BaseModel):
    title: str
    author: str
    category: Optional[str] = None
    cover_image_url: Optional[HttpUrl] = None

# API'den bir kitap döndürülürken kullanılacak şema
class BookPublic(BaseModel):
    id: uuid.UUID
    title: str
    author: str
    category: Optional[str] = None
    cover_image_url: Optional[HttpUrl] = None
    average_rating: float
    comment_count: int

    class Config:
        from_attributes = True