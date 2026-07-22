from ollama import embed

class EmbeddingService:

    @staticmethod
    def generate_embedding(text:str) -> list[float]:
        response=embed(
            model="nomic-embed-text",
            input=text
        )
        return response["embeddings"][0]