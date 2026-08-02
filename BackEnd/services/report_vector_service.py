import chromadb
from langchain_text_splitters import RecursiveCharacterTextSplitter

from knowledge_base.embeddings import generate_embeddings


class ReportVectorService:
    """
    Handles indexing generated research reports into ChromaDB.
    """

    def __init__(self):
        self.client = chromadb.PersistentClient(
            path="./knowledge_base/chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="report_chunks"
        )

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150,
        )

    def index_report(
        self,
        session_id: int,
        report: str,
    ):
        """
        Splits the report into chunks and stores them in ChromaDB.
        """

        chunks = self.text_splitter.split_text(report)

        embeddings = generate_embeddings(chunks)

        ids = []
        metadatas = []

        for index in range(len(chunks)):
            ids.append(f"{session_id}_chunk_{index}")

            metadatas.append(
                {
                    "session_id": session_id,
                    "chunk_index": index,
                }
            )

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        print(f"✅ Indexed {len(chunks)} report chunks.")