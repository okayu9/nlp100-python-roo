"""Tests for NLP 100 Exercise Chapter 1 Problem 00."""

from nlp100.ch01.q00 import reverse_string


def test_reverse_string() -> None:
    """Test for reverse_string function."""
    assert reverse_string("stressed") == "desserts"
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
