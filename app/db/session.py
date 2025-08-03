from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# 1. Veritabanı motorunu (engine) oluştur.
# Bu nesne, uygulama boyunca tek bir tane olacak ve veritabanı ile
# alt seviye iletişimi yönetecek.
# settings.DATABASE_URL, .env dosyasından okunan bağlantı bilgisidir.
# pool_pre_ping=True, uzun süre açık kalan bağlantıların kopması durumunda
# bağlantıyı kontrol edip gerekirse yenilemesini sağlar, bu da production
# ortamları için iyi bir pratiktir.
engine = create_engine(str(settings.DATABASE_URL), pool_pre_ping=True)


# 2. Veritabanı oturumları (sessions) oluşturmak için bir fabrika (factory)
# Bu, henüz bir oturumun kendisi değil, ihtiyaç duyulduğunda oturum
# yaratacak bir sınıftır.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 3. Her API isteği için bir veritabanı oturumu sağlayan Dependency
def get_db():
    """
    FastAPI Dependency: Her istek için bir veritabanı oturumu (Session) sağlar.
    İstek tamamlandığında veya bir hata oluştuğunda oturumu otomatik olarak kapatır.
    """
    db = SessionLocal()
    try:
        # 'yield' anahtar kelimesi, bu oturum nesnesini API endpoint'ine verir.
        # Endpoint'in kodu çalışırken, bu fonksiyon burada bekler.
        yield db
    finally:
        # Endpoint'in işi bittiğinde (başarılı ya da hatalı),
        # 'finally' bloğu çalışır ve veritabanı oturumu kapatılır.
        # Bu, bağlantı sızıntılarını (connection leaks) önler.
        db.close()