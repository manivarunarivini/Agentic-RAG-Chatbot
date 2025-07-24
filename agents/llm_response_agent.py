# agents/llm_response_agent.py

import torch
from transformers import pipeline

class LLMResponseAgent:
    def __init__(self):
        print("[LLMResponseAgent] Initializing model...")

        self.device = 0 if torch.cuda.is_available() else -1

        self.pipe = pipeline(
            "text2text-generation",  # <-- note: flan-t5 uses this task
            #model="tiiuae/falcon-7b-instruct",  #very large model (9B parameters)
            model="google/flan-t5-small",        # smaller model
            device=self.device
        )

        print(f"[LLMResponseAgent] Model loaded on {'GPU' if self.device == 0 else 'CPU'}")

    def generate_response(self, query: str) -> str:
        print(f"[LLMResponseAgent] Generating response for: {query}")
        result = self.pipe(query, max_new_tokens=200)[0]
        return result["generated_text"]
