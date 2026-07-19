from pydantic import BaseModel


class AIChatRequest(BaseModel):
    message:str

class AIChatResponse(BaseModel):
    response:str

class EmailGeneratorRequest(BaseModel):
    lead_name:str
    company:str
    goal:str
    tone:str