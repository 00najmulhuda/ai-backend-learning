from fastapi import APIRouter
from app.schemas.ai import AIChatRequest,AIChatResponse,EmailGeneratorRequest,SummaryGeneratorRequest
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


@router.post("/generate-email")
def generate_email(request:EmailGeneratorRequest):
    response = AIService.generate_email(request)
    return{
        "response":response
    }


@router.post("/generate-summary")
def generate_summary(request:SummaryGeneratorRequest):
    response=AIService.generate_summary(request)
    return{
        "response":response
    }