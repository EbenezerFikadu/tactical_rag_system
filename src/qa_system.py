
from typing import Dict, Any, List

class TacticalQASystem:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm
        
    def ask_question(self, question: str) -> Dict[str, Any]:
        retrieved_chunks = self.retriever.retrieve_relevant_chunks(question)
        
        if not retrieved_chunks:
            return {
                "answer": "No relevant information found.",
                "sources": [],
                "confidence": 0.0
            }
        
        context = self.retriever.format_context(retrieved_chunks)
        prompt = self._build_prompt(question, context)
        answer = self.llm.generate_response(prompt)
        
        avg_confidence = sum(chunk["similarity_score"] for chunk in retrieved_chunks) / len(retrieved_chunks)
        
        sources = [{
            "source": chunk["source"],
            "relevance_score": chunk["similarity_score"]
        } for chunk in retrieved_chunks]
        
        return {
            "answer": answer,
            "sources": sources,
            "confidence": avg_confidence
        }
    
    def _build_prompt(self, question: str, context: str) -> str:
        return f"""Use the context to answer the question accurately.

CONTEXT:
{context}

QUESTION: {question}

ANSWER:"""
