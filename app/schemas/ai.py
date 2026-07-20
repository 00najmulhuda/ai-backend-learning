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

class SummaryGeneratorRequest(BaseModel):
    text:str

class ProposalGeneratorRequest(BaseModel):
    client_name:str
    project_name:str
    project_description:str
    technologies:str
    timeline:str
    budget:str
    