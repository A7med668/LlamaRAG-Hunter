<div align="center">

# 🛡️ AI Threat Hunter
<p align="center">
  <img src="assets\Header.png"width="80%">
</p>

### AI-Powered Threat Hunting Assistant for Logs, PCAP, EVTX, JSON, TXT, and APK Analysis

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-0f172a?style=for-the-badge&logo=python&logoColor=38bdf8" />
  <img src="https://img.shields.io/badge/Streamlit-App-111827?style=for-the-badge&logo=streamlit&logoColor=ff4b4b" />
  <img src="https://img.shields.io/badge/Ollama-Llama3-111827?style=for-the-badge&logo=ollama&logoColor=ffffff" />
  <img src="https://img.shields.io/badge/ChromaDB-RAG-111827?style=for-the-badge&logoColor=22c55e" />
  <img src="https://img.shields.io/badge/MITRE_ATT%26CK-Mapped-111827?style=for-the-badge&logoColor=f59e0b" />
  <img src="https://img.shields.io/badge/Status-Active-0f172a?style=for-the-badge&logoColor=22c55e" />
</p>

<p align="center">
  <b>Designed for Blue Teams, SOC Analysts, DFIR Engineers, and Mobile Security Researchers.</b>
</p>

</div>

---

## 📌 Overview

**AI Threat Hunter** is a modular cybersecurity analysis tool built with **Streamlit**, **Ollama (Llama3)**, **ChromaDB**, and **MITRE ATT&CK RAG**.

It allows analysts to upload security artifacts such as:

- Windows Event Logs (`.evtx`)
- Network Packet Captures (`.pcap`)
- JSON / TXT / LOG files
- Android APK files (`.apk`)

The system parses the uploaded file, performs AI-assisted analysis, retrieves relevant **MITRE ATT&CK techniques**, and generates a concise threat hunting report with alerts and investigation support.

---

## ✨ Key Features

### 🔍 Threat Analysis
- AI-driven log and artifact analysis using **Ollama + Llama3**
- Suspicious behavior detection
- Confidence-based findings
- Attack pattern interpretation

### 🎯 MITRE ATT&CK Mapping
- Built-in **RAG pipeline** using **ChromaDB**
- Retrieval of relevant **Enterprise + Mobile ATT&CK techniques**
- Technique-aware contextual response generation

### 📱 APK Static Analysis
- Extracts package metadata
- Lists permissions and flags dangerous ones
- Detects suspicious API usage
- Finds hardcoded URLs and emails
- Highlights indicators like:
  - Dynamic code loading
  - Premium SMS abuse
  - Device ID harvesting
  - WebView risk patterns

### 📡 Multi-Format Support
- EVTX parsing
- PCAP summarization
- JSON / TXT / LOG ingestion
- APK inspection

### 💬 Analyst Q&A
- Ask follow-up questions about uploaded files
- Context-aware answers using LLM + MITRE technique retrieval

### 🎨 Professional Dark UI
- Custom Streamlit dark theme
- Modern SOC-style visuals
- Clean panels, alerts, tabs, and metrics

---

## 🖼️ Interface Style

The application includes a **custom professional dark theme** tailored for cybersecurity workflows:

- Deep dark blue background
- Neon-cyan action accents
- Professional alert blocks
- Styled upload zones and metric cards
- Modern hover effects and tab layouts

> Ideal for dashboards, SOC demonstrations, portfolio projects, and internal tooling prototypes.

---

## 🏗️ Project Structure

```text
ai_threat_hunter/
├── app.py                # Main Streamlit entry point
├── config.py             # Configuration constants
├── theme.py              # Professional dark theme CSS
├── llm_client.py         # Ollama wrapper
├── rag.py                # ChromaDB + embeddings + MITRE knowledge base
├── parsers/
│   ├── __init__.py
│   ├── evtx_parser.py
│   ├── pcap_parser.py
│   ├── apk_parser.py
│   └── file_reader.py    # Dispatcher for all file types
├── analysis.py           # LLM analysis, report generation, Q&A
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

---

## ⚙️ Tech Stack

| Layer | Technology |
|------|------------|
| UI | Streamlit |
| LLM | Ollama + Llama3 |
| Vector DB | ChromaDB |
| Embeddings | Sentence Transformers |
| Threat Knowledge | MITRE ATT&CK |
| APK Analysis | Androguard |
| PCAP Analysis | Scapy |
| EVTX Parsing | python-evtx |

---

## 🚀 How It Works

```text
Upload File
   ↓
Parser Selects File Type
   ↓
Content Extracted / Summarized
   ↓
Llama3 Performs Threat Analysis
   ↓
Keywords Sent to RAG Layer
   ↓
Relevant MITRE ATT&CK Techniques Retrieved
   ↓
Security Report + Alerts + Q&A
```

---

## 📂 Supported File Types

| File Type | Purpose |
|----------|---------|
| `.evtx` | Windows Event Log analysis |
| `.pcap` | Network traffic summary |
| `.json` | Structured log ingestion |
| `.txt` / `.log` | Raw text log analysis |
| `.apk` | Static Android malware / risk analysis |

---

## 🧠 Example Capabilities

### For Windows / Logs
- Detect possible PowerShell abuse
- Flag LSASS dumping indicators
- Identify failed login activity
- Summarize suspicious patterns

### For PCAP
- Extract source/destination communication
- Identify DNS queries
- Provide quick network behavior summaries

### For APK
- Inspect dangerous permissions
- Detect suspicious APIs like:
  - `Runtime.exec`
  - `DexClassLoader`
  - `sendTextMessage`
  - `getDeviceId`
  - `WebView.loadUrl`
- Extract hardcoded infrastructure indicators

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai_threat_hunter.git
cd ai_threat_hunter
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install and Start Ollama

Make sure Ollama is installed and running:

```bash
ollama serve
```

Then pull the required model:

```bash
ollama pull llama3
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🧾 Requirements

```txt
streamlit
ollama
chromadb
sentence-transformers
androguard
scapy
Evtx
```

---

## 🔧 Configuration

Edit `config.py` to customize core settings:

```python
MODEL_NAME = "llama3"
CHROMA_DB_PATH = "./chroma_db"
MAX_LOG_LEN = 3000
RAG_TOP_K = 3
```

### Config Options

| Variable | Description |
|----------|-------------|
| `MODEL_NAME` | Ollama model to use |
| `CHROMA_DB_PATH` | Persistent path for vector DB |
| `MAX_LOG_LEN` | Max content length passed to LLM |
| `RAG_TOP_K` | Number of MITRE techniques retrieved |

---

## 🧪 Example Use Cases

- Blue team triage of suspicious logs
- Investigating abnormal Windows events
- Reviewing small PCAP captures quickly
- Static inspection of Android apps
- Demonstrating AI-assisted SOC workflows
- MITRE-mapped incident review prototype

---

## 📋 Example Output

The generated report includes:

- **Analysis timestamp**
- **Detected file type**
- **LLM-generated threat assessment**
- **Relevant MITRE ATT&CK techniques**
- **Automatic alert indicators**
- **Follow-up Q&A support**

Example findings may include:

- Unusual PowerShell usage
- LSASS dumping attempt
- Dangerous APK permissions
- Premium SMS abuse potential
- Dynamic code execution
- Device identifier collection

---

## 💬 Interactive Q&A

After analysis, analysts can ask questions such as:

- `Does this APK contain dangerous permissions?`
- `Was there any LSASS access?`
- `What MITRE techniques are relevant here?`
- `Is this behavior suspicious or benign?`

The assistant answers using:
- uploaded file context
- retrieved MITRE knowledge
- Llama3 reasoning

---

## 🎨 Dark Theme Details

The custom UI theme in `theme.py` includes:

- dark navy background
- cyan primary accent
- styled sidebar
- neon-style buttons
- polished tabs and expanders
- custom input styling
- security dashboard-like metric cards

This gives the app a clean and professional **cyber defense aesthetic**.

---

## 📸 Recommended GitHub Enhancements

To make this repo even better, consider adding:

- screenshots of the dashboard
- sample EVTX / PCAP / APK reports
- animated GIF demo
- architecture diagram
- roadmap section
- sample malicious APK case study

You can create a `/screenshots` folder and reference images like this:

```md
## Dashboard Preview

<p align="center">
  <img src="./screenshots/dashboard.png" width="90%" alt="AI Threat Hunter Dashboard" />
</p>
```

---

## 🛣️ Roadmap

- [ ] Add Sigma rule suggestions
- [ ] Add IOC extraction panel
- [ ] Add YARA-style pattern detection
- [ ] Add report export to PDF / JSON
- [ ] Add severity scoring
- [ ] Add MITRE ATT&CK matrix visualization
- [ ] Add VT / OSINT enrichment
- [ ] Add multi-file correlation

---

## 🤝 Contributing

Contributions are welcome.

If you'd like to improve the project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

Ideas for contribution:
- new parsers
- better APK heuristics
- stronger MITRE mapping
- improved UI/UX
- export/reporting features

---

## ⚠️ Disclaimer

This project is intended for:

- research
- education
- defensive security analysis
- internal tooling prototypes

It should not be relied upon as a sole source of truth for incident response decisions. Always validate findings with manual investigation and additional telemetry.

---

## 📄 License

You can use the MIT License or your preferred open-source license.

Example:

```txt
MIT License
```

---

## 👨‍💻 Author

**AI Threat Hunter**  
Built for modern blue team workflows, malware triage, and AI-assisted threat analysis.

---

<div align="center">

### ⭐ If you like this project, consider giving it a star.

</div>
