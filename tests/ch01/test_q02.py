"""Tests for NLP 100 Exercise Chapter 1 Problem 02."""

from nlp100.ch01.q02 import alternate_concat


def test_alternate_concat() -> None:
    """Test for alternate_concat function."""
    # 基本ケース: 問題の例
    assert alternate_concat("パトカー", "タクシー") == "パタトクカシーー"

    # 他の基本ケース
    assert alternate_concat("abc", "def") == "adbecf"

    # 長さが異なる場合
    assert alternate_concat("abc", "de") == "adbec"
    assert alternate_concat("ab", "def") == "adbef"

    # 空文字列を含む場合
    assert alternate_concat("", "abc") == "abc"
    assert alternate_concat("abc", "") == "abc"
    assert alternate_concat("", "") == ""

    # 日本語と英語の混合
    assert alternate_concat("こんにちは", "hello") == "こhんeにlちlはo"
