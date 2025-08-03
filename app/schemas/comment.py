import uuid
from pydantic import BaseModel, Field
from typing import Optional
from .user import UserPublic # Yorumu yapan kullanıcıyı göstermek için

class CommentBase(BaseModel):
    text: str
    rating: int = Field(..., ge=1, le=5) # Puan 1 ile 5 arasında olmalı

class CommentCreate(CommentBase):
    pass

class CommentPublic(CommentBase):
    id: uuid.UUID
    book_id: uuid.UUID
    sentiment: Optional[str] = None
    summary: Optional[str] = None
    user: UserPublic # Yorumu yapan kullanıcının bilgileri

    class Config:
        from_attributes = True