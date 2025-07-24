# coordinator.py
import uuid
from agents.ingestion_agent import IngestionAgent
from agents.retrieval_agent import RetrievalAgent
from agents.llm_response_agent import LLMResponseAgent
from mcp import MCPMessage

class CoordinatorAgent:
    def __init__(self):
        self.ingestion = IngestionAgent()
        self.retrieval = RetrievalAgent()
        self.llm_response = LLMResponseAgent()

    def run(self, files, query):
        trace_id = str(uuid.uuid4())

        chunks = self.ingestion.run(files)
        retrieval_msg = MCPMessage("IngestionAgent", "RetrievalAgent", {
            "chunks": chunks,
            "query": query
        }, trace_id)

        relevant_chunks = self.retrieval.run(retrieval_msg.payload["chunks"], query)
        response_msg = MCPMessage("RetrievalAgent", "LLMResponseAgent", {
            "retrieved_context": relevant_chunks,
            "query": query
        }, trace_id)

        combined_prompt = f"Context: {response_msg.payload['retrieved_context']}\n\nQuestion: {response_msg.payload['query']}"
        answer = self.llm_response.generate_response(combined_prompt)

        return answer, relevant_chunks
