import socket
import sys
from datetime import datetime

def scan_ports(target_ip, start_port, end_port, output_file=None):
    print(f"Starting scan on host: {target_ip}")
    print(f"Scanning ports from {start_port} to {end_port}...\n")

    start_time = datetime.now()
    open_ports = []

    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port}: Open")
                open_ports.append(port)
            sock.close()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved.")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"\nScan completed in: {total_time}")

    # Write results to file if output_file is provided
    if output_file:
        with open(output_file, "a") as file:
            file.write(f"Scan results for {target_ip}:\n")
            if open_ports:
                for port in open_ports:
                    file.write(f"Port {port}: Open\n")
            else:
                file.write("No open ports found.\n")
            file.write(f"Scan completed in: {total_time}\n\n")

def scan_ip_range(start_ip, end_ip, start_port, end_port, output_file=None):
    start_ip_parts = list(map(int, start_ip.split('.')))
    end_ip_parts = list(map(int, end_ip.split('.')))

    current_ip_parts = start_ip_parts.copy()

    while current_ip_parts <= end_ip_parts:
        target_ip = ".".join(map(str, current_ip_parts))
        print(f"\nScanning IP: {target_ip}")
        scan_ports(target_ip, start_port, end_port, output_file)

        # Increment the IP address
        current_ip_parts[3] += 1
        for i in range(3, 0, -1):
            if current_ip_parts[i] > 255:
                current_ip_parts[i] = 0
                current_ip_parts[i - 1] += 1

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python port_scanner.py <start_ip> <end_ip> <start_port> <end_port> <output_file>")
        sys.exit()

    start_ip = sys.argv[1]
    end_ip = sys.argv[2]
    start_port = int(sys.argv[3])
    end_port = int(sys.argv[4])
    output_file = sys.argv[5]

    scan_ip_range(start_ip, end_ip, start_port, end_port, output_file)