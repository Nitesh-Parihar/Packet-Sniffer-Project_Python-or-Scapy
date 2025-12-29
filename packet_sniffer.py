from scapy.all import sniff, IP, TCP, UDP

def capture_packet(packet):
    # Capture Packets
    # print("-------- Capture Packets ---------------")
    print(packet.summary())
    print("\n")

    # Filter Only IP Packets
    print("---------Filter Only IP Packets ------------")
    if IP in packet:
        print("Source IP : " , packet[IP].src)
        print("Destination IP : " , packet[IP].dst)
        print("\n\n\n\n")
    
    # Capture TCP & UDP Packets
    print("-------- Capture TCP & UDP Packets ------------")
    if IP in packet:
        print("IP : ", packet[IP].src, "->", packet[IP].dst)

        if TCP in packet:
            print("Protocol: TCP")
            print("Source Port : ", packet[TCP].sport)
            print("Destination Port : ", packet[TCP].dport)

        elif UDP in packet:
            print("Protocol : UDP")
            print("Source Port : ",packet[UDP].sport)
            print("Destination Port : ", packet[UDP].dport)

    # print("----------------------------------------\n\n\n\n")

    # Save Captured Data to File (Project Enhancement)
    if IP in packet:
        with open("packet.txt","a") as file:
            file.write(f"{packet[IP].src} -> {packet[IP].dst}\n")

sniff(prn=capture_packet,count=100)
# sniff(prn=capture_packet)


# Use all protocol and filter them and save to each protocol in saprate file like TCP in TCP.log etc
# i want to sniff all packet whenever use not quit and as for save the output in the file and the file name include the timestamp o packet captature