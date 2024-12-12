import argparse
from scapy.all import IP, TCP, sr1
from tqdm import tqdm  # Import tqdm for the progress bar
from colorama import Fore, init  # Import colorama for colored text

# Initialize colorama
init(autoreset=True)

def tcp_scan(target, ports, port_range=False):
    print(f"Starting TCP scan on target: {target}")

    # If range is specified, create the range of ports
    if port_range:
        low_port, high_port = ports
        ports = range(low_port, high_port + 1)

    open_ports = []
    
    # Use tqdm for the progress bar, with colors
    for port in tqdm(ports, desc=f"{Fore.GREEN}Scanning ports...", unit="port", bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} ports", colour='green'):
        tcp_packet = IP(dst=target) / TCP(dport=port, flags="S")
        response = sr1(tcp_packet, timeout=1, verbose=False)

        if response and response.haslayer(TCP):
            if response[TCP].flags == "SA":
                open_ports.append(port)

    # Display open ports in blue
    print(f"\n{Fore.BLUE}Open ports:")
    for port in open_ports:
        print(f"{Fore.YELLOW}{port}")

def main():
    parser = argparse.ArgumentParser(description="Simple network scanner built with Scapy")

    subparsers = parser.add_subparsers(dest="command", required=True)

    tcp_parser = subparsers.add_parser("TCP", help="Perform a TCP scan using SYN packets")
    tcp_parser.add_argument("target", type=str, help="An IP address or hostname to target")
    tcp_parser.add_argument("ports", nargs="+", type=int, help="Ports to scan, delimited by spaces. Use --range for a range of ports.")
    tcp_parser.add_argument("--range", action="store_true", help="Indicate that the ports argument is a range (e.g., 0 1000)")

    args = parser.parse_args()

    if args.command == "TCP":
        if args.range:
            if len(args.ports) != 2:
                parser.error("When using --range, specify exactly two ports (low and high).")
            tcp_scan(args.target, args.ports, port_range=True)
        else:
            tcp_scan(args.target, args.ports)

if __name__ == "__main__":
    main()
