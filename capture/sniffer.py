from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS
from utils import globals
from filters.filter_engine import apply_filters
import time

def packet_handler(packet):
    if IP not in packet:
        return

    proto = "OTHER"
    if TCP in packet:
        proto = "TCP"
    elif UDP in packet:
        proto = "UDP"
    elif ICMP in packet:
        proto = "ICMP"
    elif DNS in packet:
        proto = "DNS"
    packet_data = {
        "time": time.strftime("%H:%M:%S"),
        "src": packet[IP].src,
        "dst": packet[IP].dst,
        "protocol": proto,
        "length": len(packet)
    }

    if apply_filters(packet_data):
        globals.packet_list.append(packet_data)


def start_sniffing():
    sniff(
        prn=packet_handler,
        store=False,
        stop_filter=lambda x: not globals.capture_running
    )
