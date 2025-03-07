"""Tests for NLP 100 Exercise Chapter 1 Problem 03."""

from nlp100.ch01.q03 import count_word_lengths


def test_count_word_lengths() -> None:
    """Test for count_word_lengths function."""
    # When the string is empty
    assert count_word_lengths("") == []

    # When there is only one word
    assert count_word_lengths("Hello") == [5]

    # When there are only punctuation marks
    assert count_word_lengths(",.!?") == []

    # When there are multiple spaces and punctuation marks
    assert count_word_lengths("Hello,  world! How are  you?") == [5, 5, 3, 3, 3]

    # When there are numbers
    assert count_word_lengths("I have 2 apples and 3 oranges.") == [1, 4, 1, 6, 3, 1, 7]

    # When there are Japanese characters
    assert count_word_lengths("Hello 世界 Python") == [5, 2, 6]
