#python script to scan for common open ports in Windows
#this script will only check if the ports are open, not if they are being used by a specific #service or application.

import socket

common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 443]

for port in common_ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex(('127.0.0.1', port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    sock.close()

