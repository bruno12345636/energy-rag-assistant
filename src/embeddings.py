from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)


def create_embeddings(texts):
    embeddings = model.encode(
        texts,
        normalize_embeddings=True,
        show_progress_bar=True
    )

    return embeddings


def embed_query(query):
    embedding = model.encode(
        [query],
        normalize_embeddings=True
    )

    return embedding