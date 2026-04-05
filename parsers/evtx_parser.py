def parse_evtx(file_path: str) -> str:
    try:
        from Evtx.Evtx import Evtx
        logs_text = []
        with Evtx(file_path) as log:
            for i, record in enumerate(log.records()):
                if i >= 200:
                    break
                logs_text.append(record.xml())
        return "\n".join(logs_text)
    except Exception as e:
        return f"Error reading EVTX: {e}"