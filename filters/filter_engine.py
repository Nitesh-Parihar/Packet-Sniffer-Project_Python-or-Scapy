filter_settings = {
    "protocol": "ALL",
    "ip": ""
}

def apply_filters(packet):
    # Protocol filter
    if filter_settings["protocol"] != "ALL":
        if packet["protocol"] != filter_settings["protocol"]:
            return False

    # IP filter
    if filter_settings["ip"]:
        if filter_settings["ip"] not in packet["src"] and filter_settings["ip"] not in packet["dst"]:
            return False

    return True
