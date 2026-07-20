from app.schemas.ai import EmailGeneratorRequest
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