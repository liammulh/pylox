"""Provide a Lox token class."""


class Token:
    """Define the attributes and behaviors of a token object."""

    def __init__(
        self, lox_type: str, lexeme: str, literal: str | None, line: int
    ) -> None:
        """Initialize a token object with the provided attributes.

        Args:
            lox_type: One of the types listed in the types module.
            lexeme: Blob of characters in a line.
            literal: Identifier, string, or number.
            line: Line number where we can find the token.
        """
        self.lox_type = lox_type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def to_string(self) -> str:
        """Return a string representation of a token.

        It's probably more Pythonic to use __repr__ or __str__ for this,
        but for the sake of consistency with the book, I'll do it this
        way.
        """
        return f"{self.lox_type} {self.lexeme} {self.literal}"
