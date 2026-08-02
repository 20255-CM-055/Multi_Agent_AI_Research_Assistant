import chromadb

from knowledge_base.embeddings import generate_embedding
import os

print("Current Working Directory:", os.getcwd())
print("Chroma Path:", os.path.abspath("./knowledge_base/chroma_db"))

class VectorStore:

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="./knowledge_base/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="research_documents"
        )

    def add_document(
        self,
        doc_id,
        text,
        metadata,
    ):
        self.collection.add(
            ids=[doc_id],
            documents=[text],
            embeddings=[generate_embedding(text)],
            metadatas=[metadata],
        )

    # def search(
    #     self,
    #     query,
    #     top_k=5,
    # ):
    #     embedding = generate_embedding(query)

    #     return self.collection.query(
    #         query_embeddings=[embedding],
    #         n_results=top_k,
    #     )
        
    def search_documents(
        self,
        query: str,
        top_k: int = 5,
    ):
        embedding = generate_embedding(query)

        results = self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )

        return results
    
    def count_documents(self):
        return self.collection.count()


vector_store = VectorStore()