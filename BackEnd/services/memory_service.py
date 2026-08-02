from domain.document import Document
from knowledge_base.vector_store import vector_store


class MemoryService:
    """
    Retrieves relevant documents
    from the Knowledge Base.
    """

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[Document]:
        

        results = vector_store.search_documents(
            query=query,
            top_k=top_k,
        )
        
        print("\n========== CHROMA RESULTS ==========")
        print(results)
        print("====================================\n")

        documents = []

        retrieved_docs = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]

        for text, metadata in zip(
            retrieved_docs,
            metadatas,
        ):

            documents.append(
                Document(
                    title=metadata.get(
                        "topic",
                        "Knowledge Base",
                    ),
                    url="Knowledge Base",
                    content=text,
                    source="Memory",
                )
            )

        return documents