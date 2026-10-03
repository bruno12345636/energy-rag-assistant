def chunk_text(text, chunk_size=1200, overlap=200):
    paragraphs = [
        p.strip()
        for p in text.split("\n")
        if p.strip()
    ]

    chunks = []
    current_chunk = ""

    for paragraph in paragraphs:

        if len(current_chunk) + len(paragraph) <= chunk_size:
            current_chunk += " " + paragraph

        else:
            chunks.append(current_chunk.strip())

            overlap_text = current_chunk[-overlap:]

            current_chunk = overlap_text + " " + paragraph

    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks


def create_chunks(documents):
    all_chunks = []

    for document in documents:

        chunks = chunk_text(
            document["text"]
        )

        for chunk_id, chunk in enumerate(chunks):

            all_chunks.append({
                "text": chunk,
                "page": document["page"],
                "source": document["source"],
                "chunk_id": chunk_id
            })

    return all_chunks