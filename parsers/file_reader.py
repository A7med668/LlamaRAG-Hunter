import tempfile
import os
import json
from .evtx_parser import parse_evtx
from .pcap_parser import parse_pcap
from .apk_parser import parse_apk

def read_log_file(uploaded_file) -> str:
    try:
        if uploaded_file.name.endswith('.evtx'):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.evtx') as tmp:
                tmp.write(uploaded_file.getbuffer())
                tmp_path = tmp.name
            content = parse_evtx(tmp_path)
            os.unlink(tmp_path)
        elif uploaded_file.name.endswith('.pcap'):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pcap') as tmp:
                tmp.write(uploaded_file.getbuffer())
                tmp_path = tmp.name
            content = parse_pcap(tmp_path)
            os.unlink(tmp_path)
        elif uploaded_file.name.endswith('.apk'):
            with tempfile.NamedTemporaryFile(delete=False, suffix='.apk') as tmp:
                tmp.write(uploaded_file.getbuffer())
                tmp_path = tmp.name
            content = parse_apk(tmp_path)
            os.unlink(tmp_path)
        else:
            content = uploaded_file.read().decode('utf-8', errors='ignore')
            if uploaded_file.name.endswith('.json'):
                try:
                    data = json.loads(content)
                    content = json.dumps(data, indent=2)
                except:
                    pass
        return content
    except Exception as e:
        return f"Error: {e}"