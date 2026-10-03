from src.pdf_loader import load_all_pdfs
from src.chunker import create_chunks
from src.embeddings import create_embeddings, embed_query
from src.vector_store import create_index, search
from src.rag import generate_answer


print("Cargando documentos...")

documents = load_all_pdfs()

chunks = create_chunks(documents)

texts = [
    chunk["text"]
    for chunk in chunks
]


print("Generando embeddings...")

embeddings = create_embeddings(texts)

index = create_index(embeddings)


while True:

    question = input("\nHaz una pregunta: ")

    if question.lower() == "salir":
        break

    query_embedding = embed_query(question)

    contexts = search(
        index,
        query_embedding,
        chunks,
        k=5
    )

    answer = generate_answer(
        question,
        contexts
    )

    print("\nRespuesta:")
    print(answer)

    print("\nFuentes:")

    for context in contexts:
        print(
            f"- {context['source']} "
            f"(página {context['page']})"
        )