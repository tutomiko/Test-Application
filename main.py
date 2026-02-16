import socket
import sys

def get_ipv4_address(domain: str) -> str | None:
    """
    Resolves a domain name to its IPv4 address using the socket module.

    Args:
        domain: The domain name to resolve.

    Returns:
        The IPv4 address as a string, or None if resolution fails or no IPv4 is found.
    """
    try:
        # Use socket.AF_INET to specifically request IPv4 addresses
        # The results are a list of tuples: (family, type, proto, canonname, sockaddr)
        # sockaddr is (ip_address, port) for AF_INET
        addr_info = socket.getaddrinfo(domain, None, socket.AF_INET)
        if addr_info:
            # Extract the IP address from the first result
            # addr_info[0][4] is the sockaddr tuple, addr_info[0][4][0] is the IP address
            return addr_info[0][4][0]
        else:
            # This case should ideally not be reached if getaddrinfo succeeds without error
            # but is included for completeness.
            return None
    except socket.gaierror:
        # Handle cases where the domain cannot be resolved
        return None
    except Exception as e:
        # Catch any other unexpected errors during resolution
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <domain>")
        sys.exit(1)

    domain_to_resolve = sys.argv[1]
    ipv4_address = get_ipv4_address(domain_to_resolve)

    if ipv4_address:
        print(f"IPv4 Address: {ipv4_address}")
    else:
        # If no IPv4 was found, check if the domain exists and has IPv6 addresses
        # This helps differentiate between a completely unresolvable domain and one with only IPv6.
        try:
            socket.getaddrinfo(domain_to_resolve, None, socket.AF_INET6)
            print(f"Error: No IPv4 address found for {domain_to_resolve}. Only IPv6 addresses are available.")
        except socket.gaierror:
            # If getaddrinfo for IPv6 also fails, the domain is likely unresolvable.
            print(f"Error: Could not resolve domain '{domain_to_resolve}'.")
        except Exception as e:
            # Catch any other unexpected errors during the IPv6 check
            print(f"An unexpected error occurred while checking for IPv6: {e}", file=sys.stderr)
        sys.exit(1)
