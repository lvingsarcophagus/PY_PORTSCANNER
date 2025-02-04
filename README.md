# Network Port Scanner

A Python-based network port scanner that allows scanning of IP ranges and ports, with options to save results to a file.

## Features

- Scan single IP addresses or IP ranges
- Customizable port range scanning
- Output results to both console and file
- Fast and efficient scanning with timeout handling
- Error handling for common network issues
- Progress tracking and scan duration measurement

## Prerequisites

- Python 3.6 or higher
- Standard library modules: `socket`, `sys`, `datetime`

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/port-scanner.git
cd port-scanner
```

2. No additional dependencies are required as the script uses only Python standard library modules.

## Usage

The script can be run from the command line with the following syntax:

```bash
python port_scanner.py <start_ip> <end_ip> <start_port> <end_port> <output_file>
```

### Parameters:

- `start_ip`: First IP address in the range to scan
- `end_ip`: Last IP address in the range to scan
- `start_port`: First port number to scan
- `end_port`: Last port number to scan
- `output_file`: File path to save the scan results

### Example:

```bash
python port_scanner.py 192.168.1.1 192.168.1.10 1 100 scan_results.txt
```

This will:
- Scan IP addresses from 192.168.1.1 to 192.168.1.10
- Check ports 1 through 100 on each IP
- Save results to scan_results.txt

## Output Format

The scanner provides real-time console output and saves detailed results to the specified output file. The output includes:

- Open ports for each IP address
- Scan duration
- Error messages (if any)

Example output file content:
```
Scan results for 192.168.1.1:
Port 80: Open
Port 443: Open
Scan completed in: 0:00:45.123456

Scan results for 192.168.1.2:
No open ports found.
Scan completed in: 0:00:44.234567
```

## Error Handling

The script handles common errors including:
- Invalid hostname resolution
- Connection failures
- Keyboard interrupts
- Invalid input parameters

## Security Considerations

⚠️ **Important:** This port scanner should only be used on networks and systems you own or have explicit permission to test. Unauthorized port scanning may be illegal in your jurisdiction and could result in serious consequences.

## Limitations

- Single-threaded scanning (may be slow for large IP ranges)
- Basic port status checking (open/closed only)
- No service version detection
- No UDP port scanning

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License 

## Disclaimer

This tool is for educational and authorized testing purposes only. The authors are not responsible for any misuse or damage caused by this program.
