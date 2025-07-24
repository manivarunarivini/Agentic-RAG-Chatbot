# vector_store.py
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

stored_chunks = []
faiss_index = None

def embed_text(text):
    return model.encode(text)

def save_chunks_and_embeddings(chunks):
    global stored_chunks, faiss_index
    stored_chunks = chunks
    embeddings = np.array([embed_text(chunk) for chunk in chunks]).astype("float32")
    
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss_index = index

def search_similar_chunks(query, top_k=3):
    global stored_chunks, faiss_index
    if faiss_index is None or not stored_chunks:
        return []

    query_embedding = np.array([embed_text(query)]).astype("float32")
    D, I = faiss_index.search(query_embedding, top_k)
    
    return [stored_chunks[i] for i in I[0] if i < len(stored_chunks)]
