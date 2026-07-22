from pydantic import BaseModel

class EmbeddingRequest(BaseModel):
    text:str

class EmbeddingResponse(BaseModel):
    response:list[float]