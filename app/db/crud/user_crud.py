from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate
from app.core.security import get_password_hash

def get_user_by_email(db: Session, email: str):
    """E-posta adresine göre bir kullanıcıyı bulur."""
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user: UserCreate):
    """Yeni bir kullanıcı oluşturur."""
    hashed_password = get_password_hash(user.password)
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user