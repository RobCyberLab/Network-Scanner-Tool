# 📡Network Scanner Tool🌐

## Table of Contents
1. [Introduction](#introduction)
2. [Technical Description](#technical-description)
3. [Technologies Used](#technologies-used)
4. [Main Features](#main-features)
5. [Installation](#installation)
6. [Usage Examples](#usage-examples)
7. [Possible Improvements](#possible-improvements)

## Introduction📘
The Network Scanner Tool is a powerful command-line network reconnaissance application built using Scapy. It provides a flexible and efficient method for scanning network ports, helping network administrators and security professionals identify open ports and potential vulnerabilities.

## Technical Description⚙️
The tool implements a TCP port scanning mechanism with advanced features:
- **SYN Scanning**: Uses half-open TCP scanning technique
- **Progress Visualization**: Integrated progress bar with colorful output
- **Flexible Port Scanning**: 
  - Scan specific ports
  - Scan port ranges
  - Detailed error handling

Key Technical Components:
```python
# Packet crafting example
tcp_packet = IP(dst=target) / TCP(dport=port, flags="S")
response = sr1(tcp_packet, timeout=1, verbose=False)
```

## Technologies Used💻
- **Python 3.x**
  - Network programming
  - Command-line argument parsing
- **Scapy**
  - Packet manipulation
  - Network scanning
- **Additional Libraries**
  - `tqdm`: Progress bar visualization
  - `colorama`: Colored console output
  - `argparse`: Command-line argument handling

## Main Features🌟
- **TCP Port Scanning**
  - SYN half-open scanning technique
  - Supports single port and port range scanning
- **User-Friendly Interface**
  - Colorful console output
  - Progress bar during scanning
  - Clear result presentation
- **Flexible Scanning Options**
  - Specify target IP/hostname
  - Scan multiple or range of ports

## Installation🔧
1. **Prerequisites**:
   - Python 3.7+
   - Root/Administrator privileges

2. **Required Libraries**:
   ```bash
   pip install scapy tqdm colorama
   ```

3. **Clone Repository**:
   ```bash
   git clone https://github.com/RobCyberLab/Network-Scanner-Tool.git
   cd network-scanner-tool
   ```

## Usage Examples🚀
**Scan Specific Ports**:
```bash
python network_scanner.py TCP 192.168.1.1 22 80 443
```

**Scan Port Range**:
```bash
python network_scanner.py TCP 192.168.1.1 0 1000 --range
```

## Possible Improvements🔬
- **Additional Scan Types**
  - UDP scanning
  - XMAS scan
  - FIN scan
- **Enhanced Reporting**
  - JSON/CSV output
  - Detailed port service detection
- **Performance Optimization**
  - Parallel scanning
  - Adaptive timing strategies
- **Advanced Features**
  - OS fingerprinting
  - Banner grabbing
  - Stealth scanning techniques

## Security and Legal Considerations⚖️
🚨 **Important**: 
- Use only on networks you own or have explicit permission to scan
- Unauthorized network scanning may be illegal
- Respect privacy and network usage policies
