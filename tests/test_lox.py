"""Test the main Lox module."""

# Disable these mypy rules.
# mypy: disable-error-code="method-assign"
#     ^ We want to be able to patch methods in tests.
#     ^ History behind this rule in the GitHub issue below.
#     ^ https://github.com/python/mypy/issues/2427

# Built-in libraries.
from unittest.mock import MagicMock

# Third-party dependencies.
import pytest

# In-house code.
from src.lox import Lox


def test_prints_usage(capsys) -> None:  # type: ignore
    """Ensure usage message printed if too many args supplied."""
    args = ["arg0", "arg1", "arg2 (too many)"]
    lox = Lox(args)
    with pytest.raises(SystemExit):
        lox.main()
    captured = capsys.readouterr()
    assert "usage" in captured.out.lower()


def test_runs_on_file() -> None:
    """Ensure interpreter runs on file if correct args supplied."""
    args = ["arg0", "arg1 (correct number of args for running file)"]
    lox = Lox(args)
    lox.run_file = MagicMock()
    lox.main()
    assert lox.run_file.called


def test_runs_prompt() -> None:
    """Ensure interpreter runs prompt if correct args supplied."""
    args = ["arg0 (correct number of args for REPL)"]
    lox = Lox(args)
    lox.run_prompt = MagicMock()
    lox.main()
    assert lox.run_prompt.called
