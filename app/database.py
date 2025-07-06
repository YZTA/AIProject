# app/database.py
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# .env dosyasını yükle
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL bulunamadı. .env dosyanızı kontrol edin.")

# Async engine (asyncpg ile)
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# Her request için yeni session
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Base class’ı (model tanımları bu üzerinden türeyecek)
Base = declarative_base()

# Dependency injection için yardımcı fonksiyon
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()
