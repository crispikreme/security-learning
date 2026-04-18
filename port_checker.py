import socket
target = input("Enter target IP or hostname: ")
ports = [21, 22, 80, 443, 3389]
print(f"\nScanning {target}...\n")
for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} -- OPEN")
        else:
            print(f"Port {port} -- CLOSED")
        sock.close()
    except Exception as e:
            print(f"Error on port {port}: {e}")
