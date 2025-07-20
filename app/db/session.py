from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

# Veritabanı motorunu (engine) oluştur.
# connect_args, sadece SQLite için gereklidir, PostgreSQL için kaldırılabilir ama zararı yok.
engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)

# Veritabanı oturumları oluşturmak için bir fabrika (factory)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
