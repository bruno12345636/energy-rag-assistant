import streamlit as st

from src.pdf_loader import load_uploaded_pdf
from src.chunker import create_chunks
from src.embeddings import create_embeddings, embed_query
from src.vector_store import create_index, search
from src.rag import generate_answer


st.set_page_config(
    page_title="Energy RAG Assistant",
    page_icon="⚡",
    layout="centered"
)


st.title("⚡ Energy RAG Assistant")

st.write(
    "Sube documentos PDF y haz preguntas sobre su contenido."
)


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "chunks" not in st.session_state:
    st.session_state["chunks"] = None

if "index" not in st.session_state:
    st.session_state["index"] = None


# --------------------------------------------------
# PDF UPLOAD
# --------------------------------------------------

uploaded_files = st.file_uploader(
    "Sube uno o varios PDFs",
    type="pdf",
    accept_multiple_files=True
)


# --------------------------------------------------
# PROCESAR DOCUMENTOS
# --------------------------------------------------

if uploaded_files:

    if st.button("Procesar documentos"):

        documents = []

        with st.spinner("Leyendo documentos..."):

            for uploaded_file in uploaded_files:
                documents.extend(
                    load_uploaded_pdf(uploaded_file)
                )

        chunks = create_chunks(documents)

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        with st.spinner("Generando embeddings..."):

            embeddings = create_embeddings(texts)
            index = create_index(embeddings)

        st.session_state["chunks"] = chunks
        st.session_state["index"] = index

        # Al cambiar los documentos,
        # empezamos una conversación nueva
        st.session_state["messages"] = []

        st.success(
            f"{len(uploaded_files)} documento(s) procesado(s)."
        )


# --------------------------------------------------
# CHAT
# --------------------------------------------------

if (
    st.session_state["chunks"] is not None
    and st.session_state["index"] is not None
):

    st.divider()

    st.subheader("Chat")


    # --------------------------------------------------
    # MOSTRAR CONVERSACIÓN ANTERIOR
    # --------------------------------------------------

    for message in st.session_state["messages"]:

        with st.chat_message(message["role"]):

            st.write(message["content"])

            # Mostrar también las fuentes de
            # respuestas anteriores
            if (
                message["role"] == "assistant"
                and "contexts" in message
            ):

                with st.expander("Fuentes utilizadas"):

                    for i, context in enumerate(
                        message["contexts"],
                        start=1
                    ):

                        st.markdown(
                            f"""
**Fuente {i}**

Documento: `{context["source"]}`  
Página: `{context["page"]}`  
Similitud: `{context["score"]:.3f}`
"""
                        )

                        st.write(context["text"])

                        st.divider()


    # --------------------------------------------------
    # NUEVA PREGUNTA
    # --------------------------------------------------

    question = st.chat_input(
        "Haz una pregunta sobre los documentos"
    )


    if question:

        # Guardamos el historial ANTES de añadir
        # la pregunta actual
        previous_history = list(
            st.session_state["messages"]
        )


        # --------------------------------------------------
        # MOSTRAR PREGUNTA
        # --------------------------------------------------

        st.session_state["messages"].append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)


        # --------------------------------------------------
        # CREAR CONSULTA CON CONTEXTO
        # --------------------------------------------------

        previous_user_questions = [
            message["content"]
            for message in previous_history
            if message["role"] == "user"
        ]

        # Utilizamos las dos preguntas anteriores
        # para dar contexto a la búsqueda
        recent_questions = previous_user_questions[-2:]

        retrieval_query = " ".join(
            recent_questions + [question]
        )


        # --------------------------------------------------
        # RETRIEVAL
        # --------------------------------------------------

        query_embedding = embed_query(
            retrieval_query
        )

        contexts = search(
            st.session_state["index"],
            query_embedding,
            st.session_state["chunks"],
            k=5
        )
        if not contexts:

            answer = (
                "No he encontrado suficiente información "
                "en los documentos para responder a esa pregunta."
            )
         

        else:

            answer = generate_answer(
                question,
                contexts,
                previous_history
            )


        # --------------------------------------------------
        # GENERACIÓN CON MEMORIA
        # --------------------------------------------------

        with st.chat_message("assistant"):

            with st.spinner("Generando respuesta..."):

                answer = generate_answer(
                    question,
                    contexts,
                    previous_history
                )

            st.write(answer)


            # --------------------------------------------------
            # FUENTES
            # --------------------------------------------------

            with st.expander("Fuentes utilizadas"):

                for i, context in enumerate(
                    contexts,
                    start=1
                ):

                    st.markdown(
                        f"""
**Fuente {i}**

Documento: `{context["source"]}`  
Página: `{context["page"]}`  
Similitud: `{context["score"]:.3f}`
"""
                    )

                    st.write(
                        context["text"]
                    )

                    st.divider()


        # --------------------------------------------------
        # GUARDAR RESPUESTA + FUENTES
        # --------------------------------------------------

        st.session_state["messages"].append({
            "role": "assistant",
            "content": answer,
            "contexts": contexts
        })