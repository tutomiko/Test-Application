import sys
from cli import main as cli_main

if __name__ == "__main__":
    # The original print("Hello world!") is removed as per the new requirement.
    # The cli_main function from cli.py is now the entry point.
    cli_main()
