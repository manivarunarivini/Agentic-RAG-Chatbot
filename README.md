# Agentic RAG Chatbot

An **Agentic Retrieval-Augmented Generation (RAG)** chatbot that answers user queries based on uploaded documents using modular agents and open-source LLMs. Built with Python, Streamlit, FAISS, and Hugging Face Transformers.

---

## Features

- Multi-agent architecture using **Ingestion**, **Retrieval**, and **LLM Response** agents.
- Handles multi-turn questions using persistent context.
- Uses FAISS for vector similarity search.
- Powered by local or lightweight open-source LLMs.
- Streamlit web interface for ease of interaction.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/agentic-rag-chatbot.git
cd agentic-rag-chatbot
```
2. Create and Activate a Virtual Environment
# Windows
```bash
python -m venv venv
venv\Scripts\activate
```
# macOS/Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
3. Install Dependencies
```bash
pip install -r requirements.txt
```
Note: Make sure you have faiss-cpu, sentence-transformers, transformers, accelerate, and streamlit.

Run the App
```bash
streamlit run ui/app.py
```
Opens your browser 

## Project Structure
```bash
agentic-rag-chatbot/
├── agents/
│   ├── ingestion_agent.py      # Splits uploaded files into chunks
│   ├── retrieval_agent.py      # Embeds and retrieves relevant chunks
│   └── llm_response_agent.py   # Generates responses using LLM
│
├── ui/
│   └── app.py                  # Streamlit web interface
│
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
Upload files and ask a question.

Backend calls the coordinator to:

Ingest files → split into chunks.

Retrieve relevant chunks based on the query.

Pass chunks + question to LLM for answer.

## LLM Model & Acceleration
You can run on CPU (default) or GPU by modifying accelerate or using device_map="auto".

Change model in llm_response_agent.py:
```bash
model_id = "tiiuae/falcon-rw-1b"  # or any Hugging Face compatible model
```
## Requirements (requirements.txt)
streamlit
transformers
sentence-transformers
faiss-cpu
accelerate
torch

## Example Questions
Upload your documents and ask:

"What models were used for object detection?"

"Summarize the dataset creation process."

"Explain YOLO model structure."

## Troubleshooting
Model is slow? Use a smaller model or switch to GPU in llm_response_agent.py.

IndexError in retrieval? Make sure at least one file is uploaded and indexed before querying.

📌 License
MIT License. Feel free to fork, modify, and share.

