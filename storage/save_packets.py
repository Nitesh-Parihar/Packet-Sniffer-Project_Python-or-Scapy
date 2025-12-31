import csv
from utils import globals

def save_to_csv(filename):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Table headers (same as GUI)
        writer.writerow(["Time", "Source IP", "Destination IP", "Protocol", "Length"])

        for pkt in globals.packet_list:
            writer.writerow([
                pkt["time"],
                pkt["src"],
                pkt["dst"],
                pkt["protocol"],
                pkt["length"]
            ])
