from sqlalchemy.orm import Session

# Modelleri, şemaları ve servisleri import ediyoruz
from app.db.models.comment import Comment
from app.schemas.comment import CommentCreate
from app.services import gemini_service
from app.db.crud import book_crud  # Kitap istatistiklerini güncellemek için


def create_comment_for_book(
        db: Session, comment: CommentCreate, book_id: str, user_id: str
):
    """
    Bir kitap için yeni bir yorum oluşturur. Süreç:
    1. Yorum metnini analiz için Gemini'ye gönderir.
    2. Gelen analiz sonucuyla birlikte yorumu veritabanına kaydeder.
    3. Yorumun ait olduğu kitabın istatistiklerini (ortalama puan, yorum sayısı) günceller.
    """
    # 1. Yorumu Gemini ile analiz et
    analysis_result = gemini_service.analyze_comment_with_gemini(comment.text)

    # 2. Veritabanı nesnesini oluştur
    db_comment = Comment(
        text=comment.text,
        rating=comment.rating,
        book_id=book_id,
        user_id=user_id,
        sentiment=analysis_result.get("sentiment"),
        summary=analysis_result.get("summary")
    )

    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)

    # 3. Yorum eklendikten sonra, ilgili kitabın istatistiklerini güncelle
    book_crud.update_book_stats(db=db, book_id=book_id)

    return db_comment


def get_comments_for_book(db: Session, book_id: str, skip: int = 0, limit: int = 10):
    """Bir kitaba ait tüm yorumları veritabanından listeler."""
    return db.query(Comment).filter(Comment.book_id == book_id).offset(skip).limit(limit).all()