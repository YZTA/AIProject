from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.services.llm_service import LLMService
from app.api.v1.endpoints import llm as llm_router # <-- YENİ IMPORT

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Uygulama başlıyor...")
    app.state.llm_service = LLMService()
    yield
    print("Uygulama kapanıyor...")

app = FastAPI(
    title="LLM API",
    description="Entegre bir LLM modeli içeren profesyonel bir API.",
    version="0.1.0",
    lifespan=lifespan
)

# LLM router'ını ana uygulamaya dahil et
# prefix, bu router'daki tüm endpoint'lerin /api/v1 ile başlamasını sağlar
app.include_router(llm_router.router, prefix="/api/v1", tags=["LLM"]) # <-- YENİ SATIR

@app.get("/")
def read_root():
    return {"message": "Welcome to the LLM API!"}