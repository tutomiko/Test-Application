import argparse
import socket
import sys

def check_http_status(target: str, port: int) -> str:
    """Checks if a service is running on the target host and port."""
    try:
        with socket.create_connection((target, port), timeout=2):
            return "yarp"
    except (socket.gaierror, socket.timeout, ConnectionRefusedError):
        return "narp"

def main():
    parser = argparse.ArgumentParser(
        description="A simple CLI tool for domain resolution and IP generation."
    )
    parser.add_argument(
        "action",
        nargs="?",
        default="help",
        help="Action to perform: domain (resolve domain), rand (generate random IP), or target (check service availability)."
    )
    parser.add_argument(
        "value",
        nargs="?",
        help="Value for the action (e.g., domain name for 'domain' action, or target host for 'target' action)."
    )
    parser.add_argument(
        "--target",
        type=str,
        help="Target host to check for HTTP/HTTPS service availability."
    )

    args = parser.parse_args()

    if args.target:
        http_status = check_http_status(args.target, 80)
        https_status = check_http_status(args.target, 443)
        print(f"HTTP: {http_status}")
        print(f"HTTPS: {https_status}")
    elif args.action == "domain":
        if not args.value:
            print("Please provide a domain to resolve.")
            sys.exit(1)
        try:
            ip_address = socket.gethostbyname(args.value)
            print(f"The IP address of {args.value} is {ip_address}")
        except socket.gaierror:
            print(f"Could not resolve domain: {args.value}")
            sys.exit(1)
    elif args.action == "rand":
        # This is a placeholder for random IP generation logic
        # In a real scenario, you'd generate a random IP here.
        print("Generating a random IP (not implemented yet).")
    else:
        parser.print_help()

