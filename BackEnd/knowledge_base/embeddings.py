
from sentence_transformers import SentenceTransformer

_model = None


def get_model():
    global _model

    if _model is None:
        print("Loading embedding model...")
        _model = SentenceTransformer("all-MiniLM-L6-v2")

    return _model


def generate_embedding(text: str):
    return get_model().encode(text).tolist()


def generate_embeddings(texts: list[str]):
    return get_model().encode(texts).tolist()
