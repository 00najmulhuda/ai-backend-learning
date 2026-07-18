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