import streamlit as st
from theme import set_professional_dark_theme
from llm_client import OllamaLLM
from rag import setup_rag
from parsers.file_reader import read_log_file
from analysis import generate_report, answer_question

def main():
    set_professional_dark_theme()
    st.set_page_config(page_title="AI Threat Hunter", layout="wide", page_icon="🛡️")
    st.title("🛡️ AI Threat Hunting Assistant")
    st.markdown("Upload logs, PCAP, EVTX, JSON, **or APK files** for static analysis. Generates security report with MITRE ATT&CK mapping.")
    
    with st.spinner("Connecting to Ollama and loading MITRE knowledge base..."):
        llm = OllamaLLM()
        collection, embed_model = setup_rag()
    
    uploaded_file = st.file_uploader("Choose a file (evtx, pcap, log, txt, json, apk)", 
                                      type=['evtx', 'pcap', 'log', 'txt', 'json', 'apk'])
    
    if uploaded_file is not None:
        file_ext = uploaded_file.name.split('.')[-1].lower()
        if file_ext == 'apk':
            file_type = 'apk'
        elif file_ext == 'evtx':
            file_type = 'evtx'
        elif file_ext == 'pcap':
            file_type = 'pcap'
        else:
            file_type = 'log'
        
        log_text = read_log_file(uploaded_file)
        st.subheader("📄 File Analysis Preview")
        st.text_area("Preview", log_text[:2000], height=250)
        
        col1, col2 = st.columns([1, 5])
        with col1:
            hunt_button = st.button("🔍 Start Threat Hunt", use_container_width=True)
        
        if hunt_button:
            with st.spinner("Analyzing with Llama3 and RAG..."):
                report = generate_report(llm, collection, log_text, file_type)
            
            st.subheader("📊 Security Report")
            st.write(f"**Analysis time:** {report['timestamp']}")
            st.write(f"**File type:** {report['file_type'].upper()}")
            
            with st.expander("📝 Llama3 Analysis", expanded=True):
                st.write(report['llm_analysis'])
            
            with st.expander("🎯 Related MITRE ATT&CK Techniques"):
                if report['related_mitre_techniques']:
                    for tech in report['related_mitre_techniques']:
                        st.markdown(f"- **{tech['id']}** {tech['name']}: {tech['description']}")
                else:
                    st.info("No specific techniques found.")
            
            with st.expander("🚨 Automatic Alerts"):
                if report['alerts']:
                    for alert in report['alerts']:
                        st.error(alert)
                else:
                    st.success("No obvious malicious patterns detected.")
            
            st.session_state['log_context'] = log_text
            st.session_state['report'] = report
    
    if 'log_context' in st.session_state:
        st.subheader("💬 Ask questions about the file or attack")
        user_question = st.text_input("Your question (e.g., Does this APK contain dangerous permissions? Was there any LSASS access?)")
        if user_question:
            with st.spinner("Answering..."):
                answer = answer_question(llm, collection, user_question, st.session_state['log_context'])
            st.write("**Answer:**", answer)
    
    st.sidebar.markdown("### About")
    st.sidebar.info(
        "**AI Threat Hunter**\n\n"
        "- **LLM:** Ollama + llama3\n"
        "- **RAG:** ChromaDB + MITRE ATT&CK (Enterprise + Mobile)\n"
        "- **Supported formats:** EVTX, PCAP, JSON, TXT, **APK**\n\n"
        "**APK Analysis:**\n"
        "- Extracts permissions, components, dangerous API calls, hardcoded strings\n"
        "- Detects premium SMS, dynamic code loading, device ID harvesting\n\n"
        "**First run:**\n"
        "1. `ollama serve`\n"
        "2. `ollama pull llama3`\n"
        "3. `pip install -r requirements.txt`\n"
        "4. Run this app: `streamlit run app.py`"
    )
    st.sidebar.markdown("---")
    st.sidebar.caption("Made for Blue Teams & Mobile Security | v2.0")

if __name__ == "__main__":
    main()