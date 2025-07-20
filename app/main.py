from fastapi import FastAPI

# FastAPI uygulama nesnesini oluştur
app = FastAPI(
    title="LLM API",
    description="Entegre bir LLM modeli içeren profesyonel bir API.",
    version="0.1.0",
)


# Kök endpoint (/) için bir GET isteği tanımla
@app.get("/")
def read_root():
    """
    API'nin çalışıp çalışmadığını kontrol etmek için basit bir endpoint.
    """
    return {"message": "Welcome to the LLM API!"}
