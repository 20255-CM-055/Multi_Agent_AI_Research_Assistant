from uuid import uuid4

from langchain_text_splitters import RecursiveCharacterTextSplitter

from knowledge_base.vector_store import vector_store


splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
)


def ingest_document(text: str, metadata: dict):

    chunks = splitter.split_text(text)

    for chunk in chunks:

        vector_store.add_document(
            doc_id=str(uuid4()),
            text=chunk,
            metadata=metadata,
        )

    print(
        "Documents in Chroma:",
        vector_store.count_documents(),
    )