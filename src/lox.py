"""The main module for the Lox interpreter.

Check to see how the user wants to run the interpreter. If they supply
a file, we run the interpreter on the given file. Otherwise, we drop
them into the REPL.
"""


# Built-in libraries.
from typing import List
import sys


class Lox:
    """The main class for the interpreter."""

    def __init__(self, args: List[str]) -> None:
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
            self._run_file(self.args[1])
        else:
            self._run_prompt()

    def _run_file(self, path: str) -> None:
        """Run the interpreter on the given source file.

        Args:
             path: Path to the Lox source file.
        """
        with open(path, encoding="utf-8") as f:
            source = f.read()
            self._run(source)

    def _run_prompt(self) -> None:
        """Run the REPL."""
        while True:
            try:
                source = input("Lox --> ")
                self._run(source)
            except EOFError:
                break

    @staticmethod
    def _run(source: str) -> None:
        """Run the interpreter.

        Args:
             source: Lox source code.
        """
        print(source)


if __name__ == "__main__":
    lox = Lox(sys.argv)
    lox.main()
