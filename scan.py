import socket
from concurrent.futures import ThreadPoolExecutor

def scan_network(ip):
    try:
        # Create socket with a 2-second timeout
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        
        # Attempt to connect to port 443 (HTTPS)
        s.connect((ip, 443))
        print(f"[+] {ip}:443 is OPEN")
        s.close()
    except Exception:
        # Port is closed or IP is unreachable
        print(f"[-] {ip}:443 is CLOSED")

# 1. Initialize the pool ONCE
with ThreadPoolExecutor(max_workers=20) as executor:
    with open('urls.txt', 'r') as f:
        for line in f:
            try:
                # Clean the hostname and resolve to IP
                hostname = line.strip()
                
                if not hostname: continue
                
                ip = socket.gethostbyname(hostname)
                # 2. Submit the task to the EXISTING pool
                executor.submit(scan_network, ip)
            except socket.gaierror:
                print(f"[!] Could not resolve {line.strip()}")