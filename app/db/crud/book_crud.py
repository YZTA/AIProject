from sqlalchemy.orm import Session
from sqlalchemy import func  # Ortalama ve toplam hesabı için

# Modelleri import ediyoruz
from app.db.models.book import Book
from app.db.models.comment import Comment

# Şemaları import ediyoruz
from app.schemas.book import BookCreate


def create_book(db: Session, book: BookCreate):
    """Veritabanında yeni bir kitap oluşturur."""
    db_book = Book(
        title=book.title,
        author=book.author,
        category=book.category,
        # Pydantic'in özel HttpUrl tipini veritabanına kaydetmeden önce
        # string'e çeviriyoruz.
        cover_image_url=str(book.cover_image_url) if book.cover_image_url else None
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_book(db: Session, book_id: str):
    """Verilen ID'ye göre veritabanından tek bir kitabı getirir."""
    return db.query(Book).filter(Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 100):
    """Veritabanındaki tüm kitapları sayfalama (pagination) yaparak listeler."""
    return db.query(Book).offset(skip).limit(limit).all()


def update_book_stats(db: Session, book_id: str):
    """
    Bir kitabın ortalama puanını ve yorum sayısını yeniden hesaplar ve
    veritabanındaki ilgili kitabın satırını günceller.
    Bu fonksiyon, yeni bir yorum eklendiğinde veya silindiğinde çağrılır.
    """
    # 1. Yorum sayısını veritabanından sayarak bul
    comment_count = db.query(Comment).filter(Comment.book_id == book_id).count()

    # 2. Ortalama puanı hesapla
    if comment_count > 0:
        # Önce o kitaba ait tüm puanların toplamını al
        total_rating = db.query(func.sum(Comment.rating)).filter(Comment.book_id == book_id).scalar()
        # Toplam puanı yorum sayısına bölerek ortalamayı bul
        average_rating = round(total_rating / comment_count, 2)  # Virgülden sonra 2 basamak
    else:
        # Eğer hiç yorum yoksa ortalama 0'dır
        average_rating = 0.0

    # 3. İlgili kitabı bul ve hesaplanan yeni değerlerle güncelle
    db.query(Book).filter(Book.id == book_id).update({
        Book.comment_count: comment_count,
        Book.average_rating: average_rating
    })

    # Değişiklikleri veritabanına kaydet
    db.commit()