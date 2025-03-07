"""Tests for NLP 100 Exercise Chapter 1 Problem 03."""

from nlp100.ch01.q03 import count_word_lengths


def test_count_word_lengths() -> None:
    """Test for count_word_lengths function."""
    # 空文字列の場合
    assert count_word_lengths("") == []

    # 単語が1つだけの場合
    assert count_word_lengths("Hello") == [5]

    # 句読点のみの場合
    assert count_word_lengths(",.!?") == []

    # 複数の空白や句読点を含む場合
    assert count_word_lengths("Hello,  world! How are  you?") == [5, 5, 3, 3, 3]

    # 数字を含む場合
    assert count_word_lengths("I have 2 apples and 3 oranges.") == [1, 4, 1, 6, 3, 1, 7]

    # 日本語を含む場合
    assert count_word_lengths("Hello 世界 Python") == [5, 2, 6]
