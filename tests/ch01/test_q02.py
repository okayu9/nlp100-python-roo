"""Tests for NLP 100 Exercise Chapter 1 Problem 02."""

from nlp100.ch01.q02 import alternate_concat


def test_alternate_concat() -> None:
    """Test for alternate_concat function."""
    # Basic case: Example from the problem
    assert alternate_concat("パトカー", "タクシー") == "パタトクカシーー"

    # Other basic cases
    assert alternate_concat("abc", "def") == "adbecf"

    # When lengths are different
    assert alternate_concat("abc", "de") == "adbec"
    assert alternate_concat("ab", "def") == "adbef"

    # When including empty strings
    assert alternate_concat("", "abc") == "abc"
    assert alternate_concat("abc", "") == "abc"
    assert alternate_concat("", "") == ""

    # Mix of Japanese and English
    assert alternate_concat("こんにちは", "hello") == "こhんeにlちlはo"
