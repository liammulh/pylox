"""The main module for the Lox interpreter.

Check to see how the user wants to run the interpreter. If they supply
a file, we run the interpreter on the given file. Otherwise, we drop
them into the REPL.
"""


# Built-in libraries.
from typing import List


class Lox:
    """The main class for the interpreter."""

    def __init__(self, args: List[str]):
        """Initialize interpreter with supplied arguments.

        Args:
             args: Typically, this would be our list of command line
                arguments, i.e. argv. In a test harness, we can supply
                whatever we want.
        """
        self.args = args
        self.had_error = False

    def main(self) -> None:
        """Run the interpreter."""
        if len(self.args) > 2:
            print("Usage: pylox [script]")
            raise SystemExit(64)  # Based on exit codes in sysexits.h.
        if len(self.args) == 2:
            self.run_file(self.args[1])
        else:
            self.run_prompt()

    @staticmethod
    def run_file(file: str) -> None:
        """Run the interpreter on the given source file."""
        print(file)

    @staticmethod
    def run_prompt() -> None:
        """Run the REPL."""
