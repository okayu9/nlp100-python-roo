"""Tests for NLP 100 Exercise Chapter 1 Problem 01."""

from nlp100.ch01.q01 import extract_odd_chars


def test_extract_odd_chars() -> None:
    """Test for extract_odd_chars function."""
    assert extract_odd_chars("Hello, World!") == "Hlo ol!"
    assert extract_odd_chars("Python") == "Pto"
    assert extract_odd_chars("") == ""
    assert extract_odd_chars("a") == "a"
    assert extract_odd_chars("ab") == "a"
    assert extract_odd_chars("こんにちは世界") == "こには界"
