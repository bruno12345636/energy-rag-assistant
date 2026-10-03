# ⚡ Energy RAG Assistant

## 🇪🇸 Español

### Descripción

Energy RAG Assistant es una aplicación de Inteligencia Artificial basada en **Retrieval-Augmented Generation (RAG)** que permite subir documentos PDF y realizar preguntas sobre su contenido.

La aplicación utiliza búsqueda semántica para localizar la información más relevante dentro de los documentos y posteriormente utiliza un modelo de lenguaje ejecutado localmente para generar una respuesta basada en esa información.

Todo el sistema funciona de forma local, sin necesidad de utilizar APIs de pago.

### 🚀 Funcionalidades

- Subida de múltiples documentos PDF
- Extracción automática de texto
- División del contenido en chunks
- Generación de embeddings
- Búsqueda semántica mediante FAISS
- Arquitectura Retrieval-Augmented Generation (RAG)
- LLM ejecutado localmente con Ollama
- Memoria conversacional durante la sesión
- Umbral de similitud para evitar respuestas irrelevantes
- Identificación del documento y página utilizados como fuente
- Interfaz web desarrollada con Streamlit
- Sin necesidad de APIs de pago

### 🧠 Funcionamiento

La aplicación sigue la siguiente arquitectura:

```text
Documentos PDF
      ↓
Extracción de texto
      ↓
Chunking
      ↓
Embeddings
      ↓
Índice vectorial FAISS
      ↓
Pregunta del usuario
      ↓
Búsqueda semántica
      ↓
Contexto relevante
      ↓
LLM local (Llama 3.2)
      ↓
Respuesta + fuentes
```

Cuando el usuario realiza una pregunta, esta se convierte en un embedding.

FAISS compara ese vector con los embeddings de los fragmentos de los documentos y recupera aquellos que tienen mayor similitud semántica.

Los fragmentos recuperados se utilizan como contexto para que Llama 3.2 genere una respuesta basada en la documentación.

### 🛠️ Tecnologías

- Python
- Streamlit
- Ollama
- Llama 3.2
- FAISS
- Sentence Transformers
- PyPDF
- NumPy
- Git

### 📁 Estructura del proyecto

```text
energy-rag-assistant/
│
├── app.py
├── main.py
├── requirements.txt
│
├── src/
│   ├── pdf_loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag.py
│
└── data/
```

### ⚙️ Instalación

Clonar el repositorio:

```bash
git clone https://github.com/bruno12345636/energy-rag-assistant.git
cd energy-rag-assistant
```

Crear un entorno virtual:

```bash
python -m venv venv
```

Activarlo en Windows:

```bash
venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

### 🤖 Modelo local

El proyecto utiliza Ollama para ejecutar el modelo de lenguaje de forma local.

Descargar Llama 3.2:

```bash
ollama pull llama3.2:3b
```

### ▶️ Ejecutar la aplicación

```bash
streamlit run app.py
```

Después, basta con subir uno o varios documentos PDF y realizar preguntas sobre su contenido.

### 💬 Ejemplo

Pregunta:

```text
¿Qué factores afectaron al precio de la electricidad en 2025?
```

El sistema:

1. Genera un embedding de la pregunta.
2. Busca los fragmentos más relevantes mediante FAISS.
3. Envía ese contexto al LLM local.
4. Genera una respuesta basada en los documentos.
5. Muestra el documento y la página utilizados como fuentes.

### 🎯 Objetivo del proyecto

Este proyecto ha sido desarrollado para profundizar de forma práctica en:

- Retrieval-Augmented Generation
- Large Language Models
- Embeddings
- Búsqueda vectorial
- Procesamiento de documentos
- NLP
- Inteligencia Artificial Generativa

---

# 🇬🇧 English

## Description

Energy RAG Assistant is an AI application based on **Retrieval-Augmented Generation (RAG)** that allows users to upload PDF documents and ask questions about their content.

The application uses semantic search to retrieve relevant information from the uploaded documents and a locally running language model to generate answers based on that information.

The entire system runs locally without requiring paid APIs.

## 🚀 Features

- Multiple PDF upload
- Automatic text extraction
- Text chunking
- Embedding generation
- Semantic search with FAISS
- Retrieval-Augmented Generation (RAG)
- Local LLM inference with Ollama
- Conversational memory during the session
- Similarity threshold to reduce irrelevant answers
- Document and page source attribution
- Streamlit web interface
- No paid LLM APIs required

## 🧠 Architecture

```text
PDF Documents
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embeddings
      ↓
FAISS Vector Index
      ↓
User Question
      ↓
Semantic Retrieval
      ↓
Relevant Context
      ↓
Local LLM (Llama 3.2)
      ↓
Answer + Sources
```

When the user asks a question, the application converts it into an embedding.

FAISS compares this vector with the document chunk embeddings and retrieves the most semantically relevant fragments.

These fragments are provided as context to Llama 3.2, which generates an answer based on the uploaded documents.

## 🛠️ Technologies

- Python
- Streamlit
- Ollama
- Llama 3.2
- FAISS
- Sentence Transformers
- PyPDF
- NumPy
- Git

## 📁 Project Structure

```text
energy-rag-assistant/
│
├── app.py
├── main.py
├── requirements.txt
│
├── src/
│   ├── pdf_loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── rag.py
│
└── data/
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/bruno12345636/energy-rag-assistant.git
cd energy-rag-assistant
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🤖 Local LLM

The project uses Ollama to run the language model locally.

Download Llama 3.2:

```bash
ollama pull llama3.2:3b
```

## ▶️ Run the application

```bash
streamlit run app.py
```

Upload one or more PDF documents and start asking questions.

## 💬 Example

Question:

```text
What factors affected electricity prices in 2025?
```

The system:

1. Generates an embedding of the question.
2. Retrieves relevant document chunks using FAISS.
3. Provides the retrieved context to the local LLM.
4. Generates an answer based on the documents.
5. Displays the document and page used as sources.

## 🎯 Project Goal

This project was developed to gain practical experience with:

- Retrieval-Augmented Generation
- Large Language Models
- Embeddings
- Vector search
- Document processing
- Natural Language Processing
- Generative AI
