from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.schemas.token import TokenData
from app.db.crud import user_crud

# Token'ın hangi URL'den alınacağını belirtiyoruz.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login/token")


def get_current_user(
        token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    """
    Gelen token'ı doğrular ve aktif kullanıcıyı döndürür.
    Eğer token geçersizse veya kullanıcı bulunamazsa hata fırlatır.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception

    user = user_crud.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")

    return user