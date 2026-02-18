#!/usr/bin/env python3

import argparse
import socket
import sys
import random

def resolve_domain(domain_name: str) -> str:
    """Resolves a domain name to an IP address."""
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror as e:
        raise ValueError(f"Could not resolve domain '{domain_name}': {e}") from e

def get_random_ip() -> str:
    """Generates and returns a random IPv4 address."""
    return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

def main():
    """Main function for the CLI application."""
    parser = argparse.ArgumentParser(description="CLI tool to resolve a domain name to an IP address or generate a random IP.")
    parser.add_argument("domain", nargs='?', default=None, help="The domain name to resolve, or 'rand' for a random IP.")

    args = parser.parse_args()

    if args.domain is None:
        # If no argument is provided, print help and exit
        parser.print_help(sys.stderr)
        sys.exit(1)

    try:
        if args.domain.lower() == "rand":
            ip = get_random_ip()
            print(ip)
        else:
            ip = resolve_domain(args.domain)
            print(ip)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
