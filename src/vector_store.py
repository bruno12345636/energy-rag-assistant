import faiss
import numpy as np


def create_index(embeddings):
    embeddings = np.array(embeddings, dtype="float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(dimension)

    index.add(embeddings)

    return index
def search(index, query_embedding, chunks, k=5, min_score=0.35):
    import numpy as np

    query_embedding = np.array(
        query_embedding,
        dtype="float32"
    )

    scores, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for score, idx in zip(scores[0], indices[0]):

        if idx == -1:
            continue

        if score >= min_score:
            result = chunks[idx].copy()
            result["score"] = float(score)

            results.append(result)

    return results