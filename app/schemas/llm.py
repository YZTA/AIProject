from pydantic import BaseModel

# İstek (Request) için şema
class LLMPrompt(BaseModel):
    prompt: str

# Cevap (Response) için şema
class LLMResponse(BaseModel):
    response: str