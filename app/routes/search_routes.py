from sys import prefix
from unittest import result
from app.routes.ai import router
from fastapi import APIRouter

from app.schemas.search import SearchRequest,SearchResponse
from app.services.search_service import SearchService

router = APIRouter(
    prefix="/ai",
    tags=["Search"]
)

@router.post("/search",response_model=SearchResponse)
def search(request:SearchRequest):
    result=SearchService.search(request.query)

    return SearchResponse(
        result=result["result"],
        similarity=result["similarity"]
    )