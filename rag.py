import chromadb
import streamlit as st
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer
from typing import List, Dict
from config import CHROMA_DB_PATH

# MITRE ATT&CK techniques (Enterprise + Mobile)
MITRE_DATA = [
    {"id": "T1059.001", "name": "PowerShell", "description": "Adversaries may use PowerShell for execution and lateral movement."},
    {"id": "T1003.001", "name": "LSASS Memory Dumping", "description": "Adversaries may dump LSASS memory to extract credentials."},
    {"id": "T1547.001", "name": "Registry Run Keys", "description": "Persistence via registry run keys."},
    {"id": "T1070.004", "name": "File Deletion", "description": "Adversaries may delete files to hide their tracks."},
    {"id": "T1566.001", "name": "Phishing", "description": "Spearphishing attachment."},
    {"id": "T1204.002", "name": "Malicious File", "description": "User execution of malicious file."},
    {"id": "T1055", "name": "Process Injection", "description": "Inject code into processes."},
    {"id": "T1027", "name": "Obfuscated Files", "description": "Obfuscated files or information."},
    {"id": "T1406", "name": "Accessibility Abuse", "description": "Malware uses accessibility services to perform actions like clicking on permissions."},
    {"id": "T1444", "name": "Arbitrary Code Execution", "description": "Dynamic code loading or exploitation to run arbitrary code."},
    {"id": "T1418", "name": "Input Injection", "description": "Inject touch events or keystrokes using accessibility or overlay."},
    {"id": "T1429", "name": "App Data Cloning", "description": "Access and copy sensitive data from other apps."},
    {"id": "T1411", "name": "File System Access", "description": "Unauthorized read/write of files on device."},
    {"id": "T1422", "name": "System Information Discovery", "description": "Collect device identifiers, OS version, etc."},
    {"id": "T1409", "name": "Access Notifications", "description": "Read notifications from other apps."},
    {"id": "T1447", "name": "Premium SMS", "description": "Send premium-rate SMS messages."},
]

@st.cache_resource
def setup_rag():
    embed_model = SentenceTransformer('all-MiniLM-L6-v2')
    
    class CustomEmbeddingFunction(embedding_functions.EmbeddingFunction):
        def __call__(self, input: List[str]) -> List[List[float]]:
            return embed_model.encode(input, convert_to_numpy=True).tolist()
    
    chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    collection_name = "mitre_attck_mobile"
    try:
        chroma_client.delete_collection(collection_name)
    except:
        pass
    
    collection = chroma_client.create_collection(
        name=collection_name,
        embedding_function=CustomEmbeddingFunction()
    )
    
    ids = [f"tech_{i}" for i in range(len(MITRE_DATA))]
    docs = [f"{t['id']} - {t['name']}: {t['description']}" for t in MITRE_DATA]
    metas = MITRE_DATA
    collection.add(documents=docs, metadatas=metas, ids=ids)
    return collection, embed_model

def retrieve_techniques(collection, query_text: str, top_k=3) -> List[Dict]:
    results = collection.query(query_texts=[query_text], n_results=top_k)
    techniques = []
    for i in range(len(results['ids'][0])):
        techniques.append({
            'id': results['metadatas'][0][i]['id'],
            'name': results['metadatas'][0][i]['name'],
            'description': results['metadatas'][0][i]['description']
        })
    return techniques