from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # .env dosyasından okunacak değişkenler
    PROJECT_NAME: str = "LLM API"
    API_V1_STR: str = "/api/v1"

    # SQLAlchemy veritabanı URL'i
    # Değişken adı .env dosyasıyla eşleşmeli (büyük/küçük harf duyarsız)
    DATABASE_URL: str

    # .env dosyasının kodlama formatını ve adını belirtir
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


# Ayarları projenin her yerinden kolayca erişilebilir hale getirmek için
# bir nesne örneği oluşturuyoruz.
settings = Settings()
