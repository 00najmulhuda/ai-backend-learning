from fastapi import FastAPI

from app.routes.ai import router as ai_router
from app.routes.embedding_routes import router as embedding_router
from app.routes.search_routes import router as search_router

app = FastAPI()

app.include_router(ai_router)
app.include_router(embedding_router)
app.include_router(search_router)