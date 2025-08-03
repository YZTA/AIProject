import uuid
from sqlalchemy import Column, String, DateTime, Float, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship  # relationship'i import ediyoruz
from sqlalchemy.sql import func
from app.db.base import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(255), nullable=False, index=True)
    author = Column(String(255), nullable=False, index=True)
    category = Column(String(100), nullable=True)
    cover_image_url = Column(String(512), nullable=True)

    # Bu alanlar, yeni bir yorum eklendiğinde veya silindiğinde
    # uygulama mantığı tarafından hesaplanıp güncellenecektir.
    average_rating = Column(Float, default=0.0)
    comment_count = Column(Integer, default=0)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # --- İLİŞKİNİN DİĞER YÖNÜ ---
    # Bu, bir Kitap nesnesinden, o kitaba ait tüm Yorum nesnelerine
    # ".comments" niteliği ile erişmemizi sağlar.
    # "back_populates='book'" ifadesi, Comment modelindeki 'book' ilişkisiyle
    # çift yönlü bir bağlantı kurar.
    comments = relationship("Comment", back_populates="book")