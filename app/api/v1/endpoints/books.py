from typing import List
import uuid  # book_id'nin UUID tipinde olduğunu belirtmek için
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# Veritabanı ve CRUD işlemleri
from app.db.session import get_db
from app.db.crud import book_crud
from app.db.crud import comment_crud  # Yorum CRUD fonksiyonlarını import et

# Şemalar (Pydantic Modelleri)
from app.schemas.book import BookCreate, BookPublic
from app.schemas.comment import CommentCreate, CommentPublic  # Yorum şemalarını import et

# Güvenlik ve kullanıcı modelleri
from app.db.models.user import User
from app.api.v1.dependencies import get_current_user

router = APIRouter()


# --- KİTAP ENDPOINT'LERİ ---

@router.post("/", response_model=BookPublic)
def create_new_book(
        book: BookCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)  # Güvenlik: Sadece giriş yapmış kullanıcılar
):
    """
    Yeni bir kitap oluşturur. Sadece giriş yapmış kullanıcılar erişebilir.
    """
    return book_crud.create_book(db=db, book=book)


@router.get("/", response_model=List[BookPublic])
def read_all_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Tüm kitapları listeler. Bu endpoint herkese açıktır.
    """
    books = book_crud.get_books(db, skip=skip, limit=limit)
    return books


@router.get("/{book_id}", response_model=BookPublic)
def read_book_by_id(book_id: uuid.UUID, db: Session = Depends(get_db)):
    """
    Verilen ID'ye göre tek bir kitabı getirir. Bu endpoint herkese açıktır.
    """
    db_book = book_crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı.")
    return db_book


# --- KİTABA AİT YORUM ENDPOINT'LERİ ---

@router.post("/{book_id}/comments/", response_model=CommentPublic)
def create_comment_for_a_book(
        book_id: uuid.UUID,
        comment: CommentCreate,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)  # Güvenlik: Sadece giriş yapmış kullanıcılar
):
    """
    Belirtilen kitaba yeni bir yorum ve puan ekler.
    Yorum, arka planda Gemini API kullanılarak otomatik olarak analiz edilir.
    Sadece giriş yapmış kullanıcılar yorum ekleyebilir.
    """
    # Yorum eklemeden önce kitabın veritabanında var olup olmadığını kontrol etmek iyi bir pratiktir.
    db_book = book_crud.get_book(db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Yorum yapılacak kitap bulunamadı.")

    return comment_crud.create_comment_for_book(
        db=db, comment=comment, book_id=book_id, user_id=current_user.id
    )


@router.get("/{book_id}/comments/", response_model=List[CommentPublic])
def read_comments_for_a_book(
        book_id: uuid.UUID,
        skip: int = 0,
        limit: int = 10,
        db: Session = Depends(get_db)
):
    """
    Belirtilen kitaba ait yorumları listeler. Bu endpoint herkese açıktır.
    """
    # Yorumları getirmeden önce kitabın var olup olmadığını kontrol edebiliriz.
    db_book = book_crud.get_book(db, book_id=book_id)
    if not db_book:
        raise HTTPException(status_code=404, detail="Yorumları listelenecek kitap bulunamadı.")

    comments = comment_crud.get_comments_for_book(db, book_id=book_id, skip=skip, limit=limit)
    return comments