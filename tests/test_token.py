"""Test the token module."""

# Built-in code.
from src.token import Token
from src.token_type import TokenType


def test_gets_string_representation() -> None:
    """Ensure we're able to get the string representation of a token."""
    token = Token(TokenType.VAR.name, "var", None, 100)
    string_rep = token.to_string()
    assert TokenType.VAR.name in string_rep
    assert "var" in string_rep
    assert "None" in string_rep
