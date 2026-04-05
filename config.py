# Configuration file for the AI Threat Hunter

MODEL_NAME = "llama3"          # Ollama model
CHROMA_DB_PATH = "./chroma_db" # Where ChromaDB stores vectors
MAX_LOG_LEN = 3000             # Truncation length for LLM prompts
RAG_TOP_K = 3                  # Number of MITRE techniques to retrieve