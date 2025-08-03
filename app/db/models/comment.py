import uuid
from sqlalchemy import Column, String, DateTime, Text, Float, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.base import Base


class Comment(Base):
    __tablename__ = "comments"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    book_id = Column(UUID(as_uuid=True), ForeignKey("books.id"), nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    rating = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)

    sentiment = Column(String(50), nullable=True)
    summary = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # --- DEĞİŞİKLİK BURADA ---
    # Model isimlerini doğrudan sınıf olarak değil, tırnak içinde string olarak veriyoruz.
    # Bu, Python'un import anında döngüye girmesini engeller.
    book = relationship("Book", back_populates="comments")
    user = relationship("User", back_populates="comments")
    # -------------------------