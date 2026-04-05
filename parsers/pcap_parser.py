def parse_pcap(file_path: str) -> str:
    try:
        from scapy.all import rdpcap, IP, TCP, UDP, DNS
        packets = rdpcap(file_path)
        summary = []
        for p in packets[:100]:
            if IP in p:
                src = p[IP].src
                dst = p[IP].dst
                proto = "TCP" if TCP in p else "UDP" if UDP in p else "IP"
                summary.append(f"{proto} {src} -> {dst}")
                if DNS in p and p[DNS].qr == 0:
                    summary.append(f"DNS Query: {p[DNS].qd.qname.decode()}")
        return "\n".join(summary)
    except Exception as e:
        return f"Error reading PCAP: {e}"