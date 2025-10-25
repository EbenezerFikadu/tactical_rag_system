import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

class TestTacticalRAG(unittest.TestCase):
    
    def test_vector_store_initialization(self):
        """Test that vector store can be initialized"""
        from vector_store import TacticalVectorStore
        store = TacticalVectorStore()
        self.assertIsNotNone(store)
    
    def test_retrieval_basic(self):
        """Test basic retrieval functionality"""
        # This would require mock data
        pass
    
    def test_config_loading(self):
        """Test configuration file loading"""
        import json
        with open('../config/default.json', 'r') as f:
            config = json.load(f)
        self.assertIn('model', config)
        self.assertIn('retrieval', config)

if __name__ == '__main__':
    unittest.main()
