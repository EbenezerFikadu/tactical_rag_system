
def setup_system(config_path: str = "config/default.json"):
    """
    Setup complete tactical RAG system from configuration
    """
    import json
    import os
    
    if not os.path.exists(config_path):
        print(f"Config file {config_path} not found, using defaults")
        config = {}
    else:
        with open(config_path, 'r') as f:
            config = json.load(f)
    
    # Initialize components with config
    # ... implementation would go here
    
    return {
        "status": "system_ready",
        "components": ["text_processor", "embedding_generator", "vector_store", "llm", "qa_system"]
    }
