from email import message
from multiprocessing.connection import Client
from app.schemas.ai import EmailGeneratorRequest, ProposalGeneratorRequest, SummaryGeneratorRequest
import ollama

class AIService:
    @staticmethod
    def chat(message:str) -> str:
        response = ollama.chat(
            model = "qwen2.5:3b",
            messages = [
                {
                    "role":"user",
                    "content":message
                }
            ],
            options= {
                "temperature":0.5,
                "num_predict":100
            }
        )
        return response["message"]["content"]

    @staticmethod
    def generate_email(request:EmailGeneratorRequest):
        prompt = f""" 
        write a personalized business email.
        Lead_informatio: 
        lead_name : {request.lead_name}
        company:{request.lead_company}

        requirements: 
        goal:{request.goal}
        tone:{request.tone}

        sender information:
        sender_name: {request.sender_name}
        sender_company:{request.sender_company}
        Designation: {request.sender_designation}

        Instructions:
        - Write an engaging subject line.
        - Greet the lead professionally.
        - Explain the value clearly.
        - Keep the email concise.
        - End with a professional call to action.
        - Use the sender information in the signature.
        - Return only the email without markdown or explanations.
        
        generate only the email
        """
        response = ollama.chat(
            model = "qwen2.5:3b",
            messages= [
                {
                    "role":"system",
                    "content":"you are an sales expert copywriter who write professional business email"
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ],
            options = {
                "temperature":0.7,
                "num_predict":300
            }
        )
        return response["message"]["content"]

    @staticmethod
    def generate_summary(request:SummaryGeneratorRequest):
        prompt = f"""
        summarize the following text:
        text: {request.text}
        Instruction:
        -keep the summary concise.
        -preverse the important information.
        -Return only the summary 
        """

        response= ollama.chat(
            model= "qwen2.5:3b",
            messages = [
                {
                    "role":"system",
                    "content":"you are an expert at summarizing documents clearly and accurately"

                },
                {
                    "role":"user",
                    "content":prompt
                }
            ],
            options={
                "temperature":0.3,
                "num_predict":200
            }
        )
        return response["message"]["content"]
    

    @staticmethod
    def generate_proposal(request:ProposalGeneratorRequest):
        prompt=f"""
        write a professional software project proposal.

        Client information:
        client_name:{request.client_name}

        project information:
        project: {request.project_name}
        description: {request.project_description}

        Technical requirements:
        Technologies: {request.technologies}

        project constraints:
        timeline: {request.timeline}
        budget:{request.budget}

        Instructions:
        - Start with a professional greeting.
        - Show understanding of the client's requirements.
        - Explain the proposed solution.
        - Mention the technology stack.
        - Mention timeline and budget naturally.
        - End with a professional closing.
        - Return only the proposal.
        """

        response=ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role":"system",
                    "content":"you are an experience software agency proposal writer"
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ],
            options={
                "temperature":0.6,
                "num_predict":400
            }
        )
        return response["message"]["content"]