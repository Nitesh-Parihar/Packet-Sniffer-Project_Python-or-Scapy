import tkinter as tk
from tkinter import ttk
from threading import Thread

from capture.sniffer import start_sniffing
from utils import globals
from filters.filter_engine import filter_settings
from storage.save_packets import save_to_csv


def create_gui():
    root = tk.Tk()
    root.title("Secure Packet Analyzer")
    root.geometry("900x500")

    # ---------------- PACKET TABLE ----------------
    columns = ("Time", "Source", "Destination", "Protocol", "Length")
    tree = ttk.Treeview(root, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    tree.pack(fill=tk.BOTH, expand=True)

    # ---------------- BUTTON FUNCTIONS ----------------
    def start_capture():
        globals.capture_running = True
        globals.packet_list.clear()
        tree.delete(*tree.get_children())

        Thread(target=start_sniffing, daemon=True).start()

    def stop_capture():
        globals.capture_running = False

    protocol_var = tk.StringVar(value="ALL")
    ip_var = tk.StringVar()

    def update_filters():
        filter_settings["protocol"] = protocol_var.get()
        filter_settings["ip"] = ip_var.get()

    def save_packets():
        save_to_csv("captured_packets.csv")

    # ---------------- CONTROL BAR ----------------
    control_frame = tk.Frame(root)
    control_frame.pack(fill=tk.X)

    tk.Button(control_frame, text="Start", command=start_capture).pack(side=tk.LEFT)
    tk.Button(control_frame, text="Stop", command=stop_capture).pack(side=tk.LEFT)

    tk.Label(control_frame, text="Protocol").pack(side=tk.LEFT)
    tk.OptionMenu(control_frame, protocol_var, "ALL", "TCP", "UDP", "ICMP").pack(side=tk.LEFT)

    tk.Label(control_frame, text="IP").pack(side=tk.LEFT)
    tk.Entry(control_frame, textvariable=ip_var, width=15).pack(side=tk.LEFT)

    tk.Button(control_frame, text="Apply Filter", command=update_filters).pack(side=tk.LEFT)
    tk.Button(control_frame, text="Save", command=save_packets).pack(side=tk.RIGHT)

    # ---------------- LIVE TABLE REFRESH ----------------
    def refresh_table():
        tree.delete(*tree.get_children())

        for pkt in globals.packet_list:
            # Apply filters
            if filter_settings["protocol"] != "ALL":
                if pkt["protocol"] != filter_settings["protocol"]:
                    continue

            if filter_settings["ip"]:
                if filter_settings["ip"] not in pkt["src"] and filter_settings["ip"] not in pkt["dst"]:
                    continue

            tree.insert("", tk.END, values=(
                pkt["time"],
                pkt["src"],
                pkt["dst"],
                pkt["protocol"],
                pkt["length"]
            ))

        root.after(500, refresh_table)

    # Start GUI update loop
    refresh_table()

    return root
