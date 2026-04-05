import re
from datetime import datetime
from typing import Dict, List
from config import MAX_LOG_LEN, RAG_TOP_K

def analyze_with_llm(llm, log_text: str, max_len=MAX_LOG_LEN) -> str:
    prompt = f"""You are a cybersecurity expert. Analyze the following logs or APK analysis report and output only:
- Suspicious activities / indicators
- Possible MITRE ATT&CK techniques (include mobile techniques if relevant)
- Confidence level (High/Medium/Low)

Data:
{log_text[:max_len]}
"""
    response = llm(prompt, max_tokens=1024, temperature=0.2)
    return response['choices'][0]['text'].strip()

def generate_report(llm, collection, log_text: str, file_type: str) -> Dict:
    llm_analysis = analyze_with_llm(llm, log_text)
    keywords = " ".join(re.findall(r'\b\w{4,}\b', llm_analysis))
    if not keywords:
        keywords = log_text[:500]
    from rag import retrieve_techniques
    relevant_techs = retrieve_techniques(collection, keywords, top_k=RAG_TOP_K)
    
    report = {
        "timestamp": datetime.now().isoformat(),
        "file_type": file_type,
        "llm_analysis": llm_analysis,
        "related_mitre_techniques": relevant_techs,
        "alerts": []
    }
    
    # Generic alerts
    if "PowerShell" in llm_analysis or "powershell" in log_text.lower():
        report["alerts"].append("⚠️ Alert: Unusual PowerShell usage (T1059.001)")
    if "lsass" in log_text.lower():
        report["alerts"].append("🚨 High Alert: LSASS memory dumping attempt (T1003.001)")
    if "failed login" in log_text.lower() or "logon failure" in log_text.lower():
        report["alerts"].append("🔔 Medium Alert: Multiple failed logins (T1110)")
    
    # APK-specific alerts
    if file_type == "apk":
        if "DANGEROUS" in log_text:
            report["alerts"].append("⚠️ App requests dangerous permissions (SMS, location, contacts, etc.)")
        if "Runtime.exec" in log_text or "DexClassLoader" in log_text:
            report["alerts"].append("🚨 High Alert: Dynamic code execution or command injection (T1444)")
        if "sendTextMessage" in log_text:
            report["alerts"].append("💸 Premium SMS abuse potential (T1447)")
        if "WebView.loadUrl" in log_text and "javascript" in log_text.lower():
            report["alerts"].append("🌐 WebView with potential JavaScript bridge (T1436)")
        if "getDeviceId" in log_text or "getSubscriberId" in log_text:
            report["alerts"].append("🕵️ Device identifier collection (T1422)")
    
    return report

def answer_question(llm, collection, question: str, log_context: str) -> str:
    from rag import retrieve_techniques
    techs = retrieve_techniques(collection, question, top_k=2)
    tech_context = "\n".join([f"- {t['id']} {t['name']}: {t['description']}" for t in techs])
    
    prompt = f"""Context (logs/APK report):
{log_context[:1500]}

Relevant MITRE techniques:
{tech_context}

User question: {question}

Answer concisely and accurately, mentioning MITRE techniques if possible.
"""
    response = llm(prompt, max_tokens=512, temperature=0.1)
    return response['choices'][0]['text'].strip()