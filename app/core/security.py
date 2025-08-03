from datetime import datetime, timedelta, timezone
from typing import Optional
from passlib.context import CryptContext
from jose import JWTError, jwt

from app.core.config import settings

# Şifreleri hash'lemek için kullanılacak context'i oluşturuyoruz.
# 'bcrypt' algoritmasını kullanacağımızı belirtiyoruz.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = "HS256"


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Girilen düz şifre ile veritabanındaki hash'lenmiş şifreyi karşılaştırır."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """Verilen şifreyi hash'ler."""
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Verilen veri (payload) için bir JWT access token oluşturur."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # Eğer süre belirtilmezse, 15 dakika geçerli olsun
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt