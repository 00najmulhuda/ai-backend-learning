from pydantic import BaseModel


class AIChatRequest(BaseModel):
    message:str

class AIChatResponse(BaseModel):
    response:str

class EmailGeneratorRequest(BaseModel):
    lead_name:str
    lead_company:str
    goal:str
    tone:str
    sender_name:str
    sender_company:str
    sender_designation:str