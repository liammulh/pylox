"""Provide a scanner class."""

from typing import List

from src.token import Token


class Scanner:
    """Define the attributes and behaviors of a scanner."""

    def __init__(self, source: str):
        """Initialize a scanner object with the provided attributes.

        Args:
             source: Lox source code.
        """
        self.source = source
        self.tokens: List[Token] = []
