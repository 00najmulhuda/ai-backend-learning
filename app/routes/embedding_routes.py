from fastapi import APIRouter

from app.schemas.embedding import (EmbeddingRequest,EmbeddingResponse)
from app.services.embedding_service import EmbeddingService


router = APIRouter(
    prefix="/ai",
    tags=["Embedding"]
)

@router.post("/generate-embedding",response_model=EmbeddingResponse)
def generate_embedding(request:EmbeddingRequest):
    response= EmbeddingService.generate_embedding(request.text)
    return EmbeddingResponse(response=response)  