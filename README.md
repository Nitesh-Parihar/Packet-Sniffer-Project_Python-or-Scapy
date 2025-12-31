Packet Sniffer Tool
This is a simple Python-based packet sniffer tool that allows you to capture and analyze network packets on your system.

Prerequisites
Before running the script, you must install Npcap on your system. Npcap is required for packet capture functionality on Windows systems.

Step 1: Install Npcap
Download Npcap:

Go to the official Npcap website
Download the latest version of Npcap by clicking on the Download Npcap button.

Install Npcap:
Run the downloaded installer.
Make sure to check the option Install Npcap in WinPcap API-compatible Mode (this option should be enabled by default).
Follow the on-screen instructions to complete the installation.
Note: Npcap is only required for Windows systems. If you're using Linux or macOS, you can skip this step and proceed with the instructions below.

Step 2: Install Required Python Libraries
Make sure you have Python 3.x installed on your system. You can download it from python.org
Next, install the necessary libraries required for the packet sniffer:
pip install scapy
scapy is a powerful Python library used for packet manipulation and sniffing.

Step 3: Run the Packet Sniffer Tool
Clone or Download the Script:
Clone the repository or download the Python script to your local machine.

Run the Script:
Step 1 : Open a terminal or command prompt as administrator.
Step 2 : Navigate to the folder where the script is located.
Step 3 : Run the following command:-> python main.py

This will start capturing 100 network packets on your device. 