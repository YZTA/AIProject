import uuid
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship  # relationship'i import ediyoruz
from sqlalchemy.sql import func
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # --- İLİŞKİNİN DİĞER YÖNÜ ---
    # Bu, bir Kullanıcı nesnesinden, o kullanıcının yaptığı tüm Yorum nesnelerine
    # ".comments" niteliği ile erişmemizi sağlar.
    # "back_populates='user'" ifadesi, Comment modelindeki 'user' ilişkisiyle
    # çift yönlü bir bağlantı kurar.
    comments = relationship("Comment", back_populates="user")