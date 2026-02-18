# Test-Application

A simple Python command-line interface (CLI) tool for network-related operations.

## Description

This application provides basic functionality to resolve domain names to their corresponding IP addresses and to generate random IPv4 addresses. It's designed as a straightforward utility for quick lookups and random IP generation.

## Features

*   **Domain Resolution:** Resolve a given domain name (e.g., `google.com`) to its IP address.
*   **Random IP Generation:** Generate a random, valid IPv4 address.

## Installation

To install this application, clone the repository and install it using pip:

```bash
git clone https://github.com/tutomiko/Test-Application.git
cd Test-Application
pip install .
```

Alternatively, for development, you can install it in editable mode:

```bash
pip install -e .
```

## Usage

The application can be run using Python's module execution.

### Resolving a Domain Name

To resolve a domain name to its IP address, provide the domain name as an argument:

```bash
python -m test_application google.com
```

Example Output:
```
Hello user, what we scanning today?
142.250.184.142
```

### Generating a Random IP Address

To generate a random IPv4 address, use the keyword `rand` as the argument:

```bash
python -m test_application rand
```

Example Output:
```
Hello user, what we scanning today?
192.168.1.100
```

### No Argument Provided

If no argument is provided, the application will display its help message:

```bash
python -m test_application
```

Example Output:
```
Hello user, what we scanning today?
usage: cli.py [-h] [domain]
cli.py: error: the following arguments are required: domain
```

## Dependencies

*   Python 3.8+

## License

No license file is currently present in the repository.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Contact

For any questions, please reach out via the GitHub issue tracker.
