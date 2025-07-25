# Agentic RAG Chatbot

An **Agentic Retrieval-Augmented Generation (RAG)** chatbot that answers user queries based on uploaded documents using modular agents and open-source LLMs. Built with Python, Streamlit, FAISS, and Hugging Face Transformers.

---

## Features

- Multi-agent architecture using **Ingestion**, **Retrieval**, and **LLM Response** agents.
- Handles multi-turn questions using persistent context.
- Uses FAISS for vector similarity search.
- Powered by lightweight open-source LLMs.
- Streamlit web interface for ease of interaction.

---

## Setup Instructions

1. Create and Activate a Virtual Environment
# Windows
```bash
python -m venv agentic-rag-chatbot
agentic-rag-chatbot\Scripts\activate
```
# macOS/Linux
```bash
python3 -m venv agentic-rag-chatbot
source agentic-rag-chatbot/bin/activate
```
2. Install Dependencies
```bash
pip install -r requirements.txt
```
Note: Make sure you have faiss-cpu, sentence-transformers, transformers, accelerate, and streamlit.

Run the App
```bash
streamlit run ui/app.py
```
Opens your browser: Python initiates a Streamlit server on the local machine. This server is responsible for handling the application's logic and computations.
<img width="1273" height="677" alt="chatbot1" src="https://github.com/user-attachments/assets/9dcc9b70-0ff6-4d89-b5e4-6319457e3096" />

## Project Structure
```bash
agentic-rag-chatbot/
├── agents/
│   ├── coordinator.py
│   ├── ingestion_agent.py      # Splits uploaded files into chunks
│   ├── retrieval_agent.py      # Embeds and retrieves relevant chunks
│   └── llm_response_agent.py   # Generates responses using LLM
│
├── ui/
│   └── app.py                  # Streamlit web interface
├── Agentic-RAG-Chatbot_Slides.pptx  #PPT Presentation
├── vector_store.py             # FAISS vector index storage & search
├── mcp.py                      # Model Context Protocol message class
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```
## Agent Descriptions
1. IngestionAgent
Converts uploaded documents into manageable text chunks.

Output: chunks[] passed to retrieval agent.

2. RetrievalAgent
Converts chunks into embeddings using sentence-transformers.

Stores them in FAISS index.

Finds top-k similar chunks for a query.

3. LLMResponseAgent
Takes query and context, formats them into a prompt.

Uses Hugging Face AutoModelForCausalLM or transformers pipeline to generate answer.

## vector_store.py
Contains helper functions:

save_chunks_and_embeddings(chunks) — stores chunks + embeddings in FAISS.

search_similar_chunks(query) — returns top-k similar chunks based on cosine similarity.

Uses: faiss, numpy, sentence-transformers.

## Streamlit Interface (app.py)
1. Upload files and ask a question.

2. Backend calls the coordinator to:

3. Ingest files → split into chunks.

4. Retrieve relevant chunks based on the query.

5. Pass chunks + question to LLM for answer.

## LLM Model & Acceleration
You can run on CPU (default) or GPU by modifying accelerate.

Change model in llm_response_agent.py:
```bash
model_id = "google/flan-t5-small"  # or any Hugging Face compatible model
```

## Example Questions
Upload your documents and ask:

"What models were used for object detection?"

"Summarize the dataset creation process."

"Explain YOLO model structure."


