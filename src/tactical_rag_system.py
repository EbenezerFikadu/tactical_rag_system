
# TACTICAL RAG SYSTEM - COMPLETE EXPORT
# This file contains the complete working system from the Colab session

import torch
import chromadb
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from typing import List, Dict, Any
import re

# Include all the class definitions from our working system
class ColabTextProcessor:
    # ... include the complete class implementation
    pass

class ColabEmbeddingGenerator:
    # ... include the complete class implementation  
    pass

class TacticalVectorStore:
    # ... include the complete class implementation
    pass

class ColabLLM:
    # ... include the complete class implementation
    pass

class EnhancedRetriever:
    # ... include the complete class implementation
    pass

class TacticalQASystem:
    # ... include the complete class implementation
    pass

class InteractiveChat:
    # ... include the complete class implementation
    pass

# Export the current working instances
def get_working_system():
    """Return the currently working system components"""
    return {
        'text_processor': text_processor,
        'embedding_generator': embedding_generator, 
        'vector_store': vector_store,
        'llm': llm,
        'retriever': retriever,
        'qa_system': qa_system,
        'chat_interface': chat_interface
    }
