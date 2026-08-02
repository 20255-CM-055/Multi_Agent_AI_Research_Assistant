import chromadb

from knowledge_base.embeddings import generate_embedding


# class FollowupService:
#     def __init__(self):
#         self.client = chromadb.PersistentClient(
#             path="./knowledge_base/chroma_db"
#         )

#         self.collection = self.client.get_or_create_collection(
#             name="report_chunks"
#         )


#     def retrieve_context(
#     self,
#     session_id: int,
#     question: str,
#     top_k: int = 5,
# ):
#         question_embedding = generate_embedding(question)

#         results = self.collection.query(
#             query_embeddings=[question_embedding],
#             n_results=20,
#         )

#         filtered_results = []

#         for metadata, document, distance in zip(
#             results["metadatas"][0],
#             results["documents"][0],
#             results["distances"][0],
#         ):
#             if metadata["session_id"] == session_id:
#                 filtered_results.append(
#                     {
#                         "document": document,
#                         "distance": distance,
#                         "metadata": metadata,
#                     }
#                 )

#         filtered_results.sort(key=lambda x: x["distance"])

#         return filtered_results[:top_k]
    
#     def generate_followup_answer(
#     self,
#     session_id: int,
#     question: str,
#     llm_service,
# ):
#         chunks = self.retrieve_context(
#     session_id=session_id,
#     question=question,
# )
#         context = "\n\n".join(
#     chunk["document"]
#     for chunk in chunks
# )
#         prompt = f"""
# You are an AI Research Assistant.

# Answer the user's question ONLY using the research report context below.

# If the answer is present in the context:
# - Answer clearly.
# - Be concise.
# - Do not invent information.

# If the answer is NOT present in the context:
# - First say:
# "This information is not covered in the research report."
# - Then answer using your general knowledge.
# - Clearly mention that the remaining answer comes from general knowledge.

# Research Report Context:
# {context}

# User Question:
# {question}
# """
#         answer = llm_service.generate(
#             prompt
#         )

#         return answer

class FollowupService:
    def __init__(
        self,
        llm_service,
    ):
        self.llm_service = llm_service

        self.client = chromadb.PersistentClient(
            path="./knowledge_base/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="report_chunks"
        )

    def retrieve_context(
        self,
        session_id: int,
        question: str,
        top_k: int = 5,
    ):
        question_embedding = generate_embedding(question)

        results = self.collection.query(
            query_embeddings=[question_embedding],
            n_results=20,
        )

        filtered_results = []

        for metadata, document, distance in zip(
            results["metadatas"][0],
            results["documents"][0],
            results["distances"][0],
        ):
            if metadata["session_id"] == session_id:
                filtered_results.append(
                    {
                        "document": document,
                        "distance": distance,
                        "metadata": metadata,
                    }
                )

        filtered_results.sort(key=lambda x: x["distance"])

        return filtered_results[:top_k]

    def generate_followup_answer(
        self,
        session_id: int,
        question: str,
    ):
        chunks = self.retrieve_context(
            session_id=session_id,
            question=question,
        )

        context = "\n\n".join(
            chunk["document"]
            for chunk in chunks
        )

        prompt = f"""
You are an AI Research Assistant.

Answer the user's question ONLY using the research report context below.

Rules:
- If the answer exists in the report context, answer from the report.
- Do not invent information.
- If the report does not contain the answer:
    - First say:
      "This information is not covered in the research report."
    - Then answer using your general knowledge.
    - Clearly mention that the remaining answer is based on general knowledge.

Research Report Context:
{context}

User Question:
{question}
"""

        answer = self.llm_service.generate(prompt)

        return answer