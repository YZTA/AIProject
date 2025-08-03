from fastapi import APIRouter, Request, Depends
from app.schemas.llm import LLMPrompt, LLMResponse
from app.services.llm_service import LLMService

router = APIRouter()


def get_llm_service(request: Request) -> LLMService:
    """
    Uygulama state'inden LLM servisini almak için bir dependency.
    """
    return request.app.state.llm_service


@router.post("/generate", response_model=LLMResponse)
def generate_text(
        request_body: LLMPrompt,
        llm_service: LLMService = Depends(get_llm_service)
):
    """
    Bir prompt alır ve LLM'den üretilmiş bir metin döndürür.
    """
    prompt = request_body.prompt
    generated_text = llm_service.generate_response(prompt)

    return {"response": generated_text}