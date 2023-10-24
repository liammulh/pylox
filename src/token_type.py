"""List the tokens in the Lox programming language."""

from enum import Enum


class TokenType(Enum):
    """Enumerate tokens and their values.

    We know the value of most tokens ahead of time, so we record them
    here. Some of the values are placeholder values.
    """

    # Single-character tokens.
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    COMMA = ","
    DOT = "."
    MINUS = "-"
    PLUS = "+"
    SEMICOLON = ";"
    SLASH = "/"
    STAR = "*"

    # One or two character tokens.
    BANG = "!"
    BANG_EQUAL = "!="
    EQUAL = "="
    EQUAL_EQUAL = "=="
    GREATER = ">"
    GREATER_EQUAL = ">="
    LESS = "<"
    LESS_EQUAL = "<="

    # Literals. The values here are just placeholders.
    IDENTIFIER = "identifier"
    STRING = "string"
    NUMBER = "number"

    # Keywords.
    AND = "and"
    CLASS = "class"
    ELSE = "else"
    FALSE = "false"
    FUN = "fun"
    FOR = "for"
    IF = "if"
    NIL = "nil"
    OR = "or"
    PRINT = "print"
    RETURN = "return"
    SUPER = "super"
    THIS = "this"
    TRUE = "true"
    VAR = "var"
    WHILE = "while"

    # Finally, end of file. Not sure what the value should be.
    # TODO: Change this?
    EOF = "eof"
