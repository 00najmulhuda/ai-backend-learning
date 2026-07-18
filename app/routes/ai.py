from fastapi import APIRouter
from app.schemas.ai import AIChatRequest
from app.services.ai_service import AIService


router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)

@router.post("/chat")
def chat(request:AIChatRequest):
    response = AIService.chat(request.message)
    return{
        "response":response 
    }