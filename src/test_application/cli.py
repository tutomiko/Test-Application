import argparse
import sys
import random
import ipaddress

def main():
    parser = argparse.ArgumentParser(description="A test application with various commands.")
    subparsers = parser.add_subparsers(dest="action", help="Available actions")

    # Domain command
    domain_parser = subparsers.add_parser("domain", help="Process a domain name")
    domain_parser.add_argument("name", type=str, help="The domain name to process")

    # Rand command
    rand_parser = subparsers.add_parser("rand", help="Generate a random number")
    rand_parser.add_argument("--min", type=int, default=0, help="Minimum value for random number")
    rand_parser.add_argument("--max", type=int, default=100, help="Maximum value for random number")

    # Dumb command - as requested by the issue
    dumb_parser = subparsers.add_parser("dumb", help="A really dumb feature that prints a silly message.")

    # IPRange command
    iprange_parser = subparsers.add_parser('iprange', help='Process an IPv4 range')
    iprange_parser.add_argument('range_str', type=str, help='IPv4 range in CIDR (e.g., 192.168.1.0/24) or start-end (e.g., 192.168.1.1-192.168.1.255) format')

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    if args.action == "domain":
        print(f"Processing domain: {args.name.upper()}")
    elif args.action == "rand":
        if args.min >= args.max:
            print("Error: --min must be less than --max", file=sys.stderr)
            sys.exit(1)
        print(f"Generated random number: {random.randint(args.min, args.max)}")
    elif args.action == "dumb":
        print("This is a really dumb feature!")
    elif args.action == 'iprange':
        range_str = args.range_str
        try:
            # Try CIDR notation first
            network = ipaddress.IPv4Network(range_str, strict=False)
            # .hosts() excludes network and broadcast addresses, which is generally preferred for listing usable IPs
            hosts = list(network.hosts())
            if hosts:
                print(f"IPs in range {range_str} ({len(hosts)} addresses):")
                for ip in hosts:
                    print(str(ip))
            else:
                # Handle cases like /31 or /32 where .hosts() might be empty but network is valid
                if network.num_addresses == 1:
                    print(f"IP in range {range_str} (1 address):")
                    print(str(network.network_address))
                elif network.num_addresses == 2 and network.prefixlen == 31:
                    # For /31, network and broadcast are usable IPs
                    print(f"IPs in range {range_str} (2 addresses):")
                    print(str(network.network_address))
                    print(str(network.broadcast_address))
                else:
                    print(f"No usable IPs found in range {range_str}.", file=sys.stderr)
                    sys.exit(1)
        except ipaddress.AddressValueError:
            # If not CIDR, try start-end range
            if '-' in range_str:
                try:
                    start_ip_str, end_ip_str = range_str.split('-')
                    start_ip = ipaddress.IPv4Address(start_ip_str.strip())
                    end_ip = ipaddress.IPv4Address(end_ip_str.strip())

                    if start_ip > end_ip:
                        print(f"Error: Start IP ({start_ip}) cannot be greater than End IP ({end_ip}).", file=sys.stderr)
                        sys.exit(1)

                    print(f"IPs in range {range_str}:")
                    current_ip = int(start_ip)
                    while current_ip <= int(end_ip):
                        print(str(ipaddress.IPv4Address(current_ip)))
                        current_ip += 1
                except ValueError:
                    print(f"Error: Invalid start-end IPv4 range format: {range_str}. Expected format: 192.168.1.1-192.168.1.255", file=sys.stderr)
                    sys.exit(1)
                except ipaddress.AddressValueError as e:
                    print(f"Error: Invalid IPv4 address in range '{range_str}': {e}", file=sys.stderr)
                    sys.exit(1)
            else:
                print(f"Error: Invalid IPv4 range format: {range_str}. Expected CIDR (e.g., 192.168.1.0/24) or start-end (e.g., 192.168.1.1-192.168.1.255).", file=sys.stderr)
                sys.exit(1)
        except Exception as e:
            print(f"An unexpected error occurred: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # This case handles when an action is not specified but other args might be present
        # or if an unknown action is passed. argparse handles unknown actions by default
        # but this ensures a fallback for general help if 'action' is None due to some parsing edge case.
        parser.print_help(sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
