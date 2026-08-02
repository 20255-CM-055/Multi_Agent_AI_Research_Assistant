# from sentence_transformers import SentenceTransformer

# _model = SentenceTransformer("all-MiniLM-L6-v2")


# def generate_embedding(text: str):
#     """
#     Generate an embedding vector for the given text.
#     """
#     return _model.encode(text).tolist()



from sentence_transformers import SentenceTransformer

_model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text: str):
    return _model.encode(text).tolist()


def generate_embeddings(texts: list[str]):
    return _model.encode(texts).tolist()