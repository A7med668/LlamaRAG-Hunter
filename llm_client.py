import ollama
import streamlit as st
from config import MODEL_NAME

class OllamaLLM:
    def __init__(self, model_name=MODEL_NAME):
        self.model_name = model_name
        try:
            ollama.list()
        except Exception as e:
            st.error(f"⚠️ Cannot connect to Ollama: {e}\nMake sure Ollama server is running (ollama serve) and model pulled (ollama pull {model_name})")
    
    def __call__(self, prompt: str, max_tokens=1024, temperature=0.2, stop=None):
        response = ollama.generate(
            model=self.model_name,
            prompt=prompt,
            options={
                "num_predict": max_tokens,
                "temperature": temperature,
                "stop": stop if stop else []
            }
        )
        return {"choices": [{"text": response["response"]}]}