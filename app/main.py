from contextlib import asynccontextmanager
from fastapi import FastAPI

# Backend servislerimizi ve router'larımızı import ediyoruz
from app.api.v1.endpoints import users as users_router
from app.api.v1.endpoints import books as books_router
# from app.api.v1.endpoints import comments as comments_router # Henüz yok, sonra eklenecek

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Uygulama yaşam döngüsünü yönetir. Başlangıçta kaynakları yükler ve bitişte temizler.
    """
    print("Uygulama başlıyor...")
    # Gelecekte Gemini servisi gibi başlangıçta yüklenmesi gereken
    # servisler buraya eklenebilir.
    yield
    print("Uygulama kapanıyor...")


# FastAPI ana uygulama nesnesini oluşturuyoruz.
app = FastAPI(
    title="BookSense - Kitap Yorum Analiz Platformu",
    description="Kullanıcıların kitap ekleyip yorum yapabildiği, yorumların yapay zeka ile analiz edildiği bir platform.",
    version="1.0.0",
    lifespan=lifespan
)

# === ROUTER'LARI DAHİL ETME ===
# Projemizin farklı bölümlerini yöneten router'ları ana uygulamaya bağlıyoruz.

# 1. Kullanıcı Yönetimi Router'ı (Kayıt Ol, Giriş Yap)
# Bu router, `/api/v1/users` ön eki ile başlar.
app.include_router(
    users_router.router,
    prefix="/api/v1/users",
    tags=["API - Users & Authentication"]
)

# 2. Kitap Yönetimi Router'ı (Kitap Ekle, Listele)
# Bu router, `/api/v1/books` ön eki ile başlar.
app.include_router(
    books_router.router,
    prefix="/api/v1/books",
    tags=["API - Books"]
)

# Gelecekte eklenecek diğer router'lar için yer tutucu:
# app.include_router(comments_router.router, prefix="/api/v1/comments", tags=["API - Comments"])


# API'nin kök endpoint'i
@app.get("/")
def read_root():
    """
    API'nin çalıştığını belirten basit bir hoş geldiniz mesajı.
    """
    return {"message": "Welcome to the BookSense API!"}