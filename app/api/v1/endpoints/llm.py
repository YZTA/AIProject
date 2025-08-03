from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session

from app.schemas.llm import LLMPrompt, LLMResponse
from app.services.llm_service import LLMService
from app.db.session import get_db
from app.db.models.history import History  # History modelini import et

router = APIRouter()


def get_llm_service(request: Request) -> LLMService:
    return request.app.state.llm_service


@router.post("/generate", response_model=LLMResponse)
def generate_text(
        request_body: LLMPrompt,
        llm_service: LLMService = Depends(get_llm_service),
        db: Session = Depends(get_db)  # <-- Veritabanı oturumunu ekle
):
    prompt = request_body.prompt
    generated_text = llm_service.generate_response(prompt)

    # Veritabanına kaydet
    db_history = History(prompt=prompt, response=generated_text)
    db.add(db_history)
    db.commit()
    db.refresh(db_history)

    print(f"ID'si {db_history.id} olan kayıt veritabanına eklendi.")

    return {"response": generated_text}