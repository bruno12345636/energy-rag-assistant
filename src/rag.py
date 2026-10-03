from ollama import chat


def generate_answer(question, contexts, history=None):

    if history is None:
        history = []

    context_text = "\n\n".join(
        [
            f"""
Documento: {context["source"]}
Página: {context["page"]}

{context["text"]}
"""
            for context in contexts
        ]
    )

    system_prompt = f"""
Eres un asistente especializado en energía y mercado eléctrico.

Estás manteniendo una conversación con el usuario, por lo que debes
tener en cuenta las preguntas y respuestas anteriores.

Para responder preguntas sobre los documentos, utiliza únicamente
la información recuperada en el contexto.

Si la información necesaria no aparece en el contexto, indica
claramente que no dispones de suficiente información.

CONTEXTO RECUPERADO:

{context_text}
"""

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # Añadimos parte del historial.
    # Limitamos a los últimos 6 mensajes para no hacer crecer
    # demasiado el prompt.
    for message in history[-6:]:

        messages.append({
            "role": message["role"],
            "content": message["content"]
        })

    # Pregunta actual
    messages.append({
        "role": "user",
        "content": question
    })

    response = chat(
        model="llama3.2:3b",
        messages=messages
    )

    return response.message.content