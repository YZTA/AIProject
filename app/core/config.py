from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # .env dosyasından okunacak değişkenler
    PROJECT_NAME: str = "BookSense"
    API_V1_STR: str = "/api/v1"

    # SQLAlchemy veritabanı URL'i
    DATABASE_URL: str

    # --- YENİ EKLENEN ALAN ---
    # Google Gemini API Anahtarı
    # .env dosyasındaki GEMINI_API_KEY değişkenini bu alana atayacak.
    GEMINI_API_KEY: str

    # --- YENİ EKLENEN ALAN (GÜVENLİK İÇİN) ---
    # JWT token'larını imzalamak için kullanılacak gizli anahtar.
    # Bu, kullanıcı kimlik doğrulama sistemi için gereklidir.
    # Terminalde `openssl rand -hex 32` komutu ile güvenli bir anahtar üretebilirsiniz.
    SECRET_KEY: str

    # Token'ın geçerlilik süresi (dakika olarak)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 gün

    # .env dosyasının kodlama formatını ve adını belirtir
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Ayarları projenin her yerinden kolayca erişilebilir hale getirmek için
# bir nesne örneği oluşturuyoruz.
settings = Settings()