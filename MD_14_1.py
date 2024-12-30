from scapy.all import IP, TCP, sr1
from multiprocessing import Pool

def scan_port(ip, port):
    """Scan a single port on the target IP."""
    ip_pkt = IP(dst=ip)
    tcp_pkt = TCP(dport=port, flags="S")
    
    pkt = ip_pkt / tcp_pkt
    resp = sr1(pkt, timeout=1, verbose=0)

    if resp is not None and resp.haslayer(TCP):
        if resp.getlayer(TCP).flags == 0x12:  # SYN-ACK
            return port, True  # Port is open
        elif resp.getlayer(TCP).flags == 0x14:  # RST-ACK
            return port, False  # Port is closed
    return port, False  # No response means closed

def scan_ports(ip, ports):
    """Scan a list of ports on the target IP using multiprocessing."""
    with Pool(processes=len(ports)) as pool:
        results = pool.starmap(scan_port, [(ip, port) for port in ports])
    
    for port, status in results:
        if status:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")

if __name__ == "__main__":
    target_ip = "85.254.73.240"  # Mana izvēlētā IP adrese
    ports_to_scan = [22, 80, 139, 143, 443, 445, 5001, 8080, 8081]  # To scan only these ports

    print(f"Scanning {target_ip} for ports {ports_to_scan}...")
    scan_ports(target_ip, ports_to_scan)

# Output: Port 22: Closed
#         Port 80: Closed
#         Port 139: Closed
#         Port 143: Closed
#         Port 443: Closed
#         Port 445: Closed
#         Port 5001: Closed
#         Port 8080: Closed
#         Port 8081: Closed

# Šajā piemērā ir izmantots multiprocessing modulis, 
# lai skenētu vairākus portus vienlaicīgi. 
# Atbilst Uzdevumam Nr.14, bet skanēti tiek tikai devini porti.
