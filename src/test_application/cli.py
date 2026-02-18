import argparse
import sys
import random

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
    else:
        # This case handles when an action is not specified but other args might be present
        # or if an unknown action is passed. argparse handles unknown actions by default
        # but this ensures a fallback for general help if 'action' is None due to some parsing edge case.
        parser.print_help(sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
