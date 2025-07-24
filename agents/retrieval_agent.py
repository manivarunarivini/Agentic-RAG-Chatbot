from vector_store import save_chunks_and_embeddings, search_similar_chunks

class RetrievalAgent:
    def run(self, chunks, query):
        save_chunks_and_embeddings(chunks)  # ✅ Correct function name
        return search_similar_chunks(query)
