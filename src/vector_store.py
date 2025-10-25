
import chromadb
import numpy as np
from typing import List, Dict, Any

class TacticalVectorStore:
    def __init__(self, collection_name: str = "tactical_documents"):
        self.collection_name = collection_name
        self.client = None
        self.collection = None
        
    def initialize_client(self):
        self.client = chromadb.Client()
        try:
            self.collection = self.client.get_collection(self.collection_name)
        except:
            self.collection = self.client.create_collection(
                name=self.collection_name,
                metadata={"description": "Tactical documents RAG system"}
            )
    
    def add_documents(self, chunks: List[Dict], embeddings: np.ndarray):
        if self.client is None:
            self.initialize_client()
        
        documents = [chunk["content"] for chunk in chunks]
        metadatas = [chunk["metadata"] for chunk in chunks]
        ids = [f"chunk_{i}_{chunk['metadata']['source'].replace('.', '_')}" 
               for i, chunk in enumerate(chunks)]
        
        self.collection.add(
            embeddings=embeddings.tolist(),
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
    
    def query(self, query_text: str, n_results: int = 3):
        if self.collection is None:
            self.initialize_client()
        
        return self.collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
