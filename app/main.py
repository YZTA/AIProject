from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from .database import engine, Base, get_db
from .routers import users

app = FastAPI(title="FastAPI + PostgreSQL Demo")

@app.on_event("startup")
async def on_startup():
    # Veritabanı tablolarını oluştur (development için)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/")
async def read_root():
    return {"message": "Merhaba FastAPI + PostgreSQL!"}

@app.get("/ping-db")
async def ping_db(db: AsyncSession = Depends(get_db)):
    # Basit bir sorgu ile DB bağlantısını test et
    result = await db.execute("SELECT 1")
    return {"db_response": result.scalar_one()}

# CRUD router'ını dahil et
app.include_router(users.router)
