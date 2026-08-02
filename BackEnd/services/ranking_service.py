from sklearn.metrics.pairwise import cosine_similarity

from domain.document import Document
# from knowledge_base.embeddings import generate_embedding
from knowledge_base.embeddings import (
    generate_embedding,
    generate_embeddings,
)

class RankingService:

    def rank(
        self,
        query: str,
        documents: list[Document],
    ) -> list[Document]:

        if not documents:
            return []

        # query_embedding = generate_embedding(query)

        # document_embeddings = [
        #     generate_embedding(doc.content)
        #     for doc in documents
        # ]
        query_embedding = generate_embedding(query)

        document_embeddings = generate_embeddings(
            [doc.content for doc in documents]
        )

        similarities = cosine_similarity(
            [query_embedding],
            document_embeddings,
        )[0]

        ranked = sorted(
            zip(documents, similarities),
            key=lambda x: x[1],
            reverse=True,
        )

        return [doc for doc, _ in ranked]