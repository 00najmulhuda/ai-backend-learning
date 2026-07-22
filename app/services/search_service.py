from app.data.documents import documents
from app.services.embedding_service import EmbeddingService
from app.services.similarity_service import SimilarityService


class SearchService:
    @staticmethod
    def search(query:str):
        query_embedding=EmbeddingService.generate_embedding(query)

        best_document =""
        best_similarity=-1

        for document in documents:

            document_embedding=EmbeddingService.generate_embedding(document)

            similarity = SimilarityService.cosine_similarity(
                query_embedding,
                document_embedding
            )

            if similarity>best_similarity:
                best_similarity = similarity
                best_document=document

        return {
            "result":best_document,
            "similarity":best_similarity
        }