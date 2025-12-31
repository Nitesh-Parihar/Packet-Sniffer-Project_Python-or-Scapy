import csv
import os
from datetime import datetime
from utils import globals


def save_to_csv():
    # Create folder if it does not exist
    os.makedirs("captures", exist_ok=True)

    # Create unique timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"captures/packets_{timestamp}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Time",
            "Source IP",
            "Destination IP",
            "Protocol",
            "Length"
        ])

        for pkt in globals.packet_list:
            writer.writerow([
                pkt["time"],
                pkt["src"],
                pkt["dst"],
                pkt["protocol"],
                pkt["length"]
            ])

    return filename
