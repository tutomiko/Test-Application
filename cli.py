#!/usr/bin/env python3

import argparse
import socket
import sys

def resolve_domain(domain_name: str) -> str:
    """Resolves a domain name to an IP address."""
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror as e:
        raise ValueError(f"Could not resolve domain '{domain_name}': {e}") from e

def main():
    """Main function for the CLI application."""
    parser = argparse.ArgumentParser(description="CLI tool to resolve a domain name to an IP address.")
    parser.add_argument("domain", help="The domain name to resolve.")

    args = parser.parse_args()

    try:
        ip = resolve_domain(args.domain)
        print(ip)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
