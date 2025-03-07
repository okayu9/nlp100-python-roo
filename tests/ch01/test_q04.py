"""Tests for NLP 100 Exercise Chapter 1 Problem 04."""

from nlp100.ch01.q04 import create_element_map


def test_create_element_map() -> None:
    """Test for create_element_map function."""
    # 空文字列の場合
    assert create_element_map("") == {}

    # 単語が1つだけの場合(1番目の単語なので1文字取る)
    assert create_element_map("Hello", {1}) == {"H": 1}

    # 複数の単語を含む場合(1番目は1文字、それ以外は2文字)
    assert create_element_map("Hi World", {1}) == {"H": 1, "Wo": 2}

    # 問題文の例
    text = (
        "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might "
        "Also Sign Peace Security Clause. Arthur King Can."
    )
    one_char_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}
    result = create_element_map(text, one_char_positions)

    # 1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字
    assert result["H"] == 1  # Hi (1番目)
    assert result["B"] == 5  # Boron (5番目)  # noqa: PLR2004
    assert result["C"] == 6  # Could (6番目)  # noqa: PLR2004
    assert result["N"] == 7  # Not (7番目)  # noqa: PLR2004
    assert result["O"] == 8  # Oxidize (8番目)  # noqa: PLR2004
    assert result["F"] == 9  # Fluorine. (9番目)  # noqa: PLR2004
    assert result["P"] == 15  # Peace (15番目)  # noqa: PLR2004
    assert result["S"] == 16  # Security (16番目)  # noqa: PLR2004
    assert result["K"] == 19  # King (19番目)  # noqa: PLR2004

    # それ以外の単語は先頭の2文字
    assert result["He"] == 2  # He (2番目)  # noqa: PLR2004
    assert result["Li"] == 3  # Lied (3番目)  # noqa: PLR2004
    assert result["Be"] == 4  # Because (4番目)  # noqa: PLR2004
    assert result["Ne"] == 10  # New (10番目)  # noqa: PLR2004
    assert result["Na"] == 11  # Nations (11番目)  # noqa: PLR2004
    assert result["Mi"] == 12  # Might (12番目)  # noqa: PLR2004
    assert result["Al"] == 13  # Also (13番目)  # noqa: PLR2004
    assert result["Si"] == 14  # Sign (14番目)  # noqa: PLR2004
    assert result["Cl"] == 17  # Clause. (17番目)  # noqa: PLR2004
    assert result["Ar"] == 18  # Arthur (18番目)  # noqa: PLR2004
    assert result["Ca"] == 20  # Can. (20番目)  # noqa: PLR2004

    # 別のパターンでテスト
    # すべての単語の先頭1文字を取る場合
    all_positions = set(range(1, 21))
    result_all_one = create_element_map(text, all_positions)
    assert result_all_one["H"] == 2  # noqa: PLR2004  # He (2番目) - 重複するため上書きされる
    assert result_all_one["H"] != 1  # Hi (1番目) - 重複するため上書きされる

    # すべての単語の先頭2文字を取る場合
    result_all_two = create_element_map(text, set())
    assert result_all_two["Hi"] == 1  # Hi (1番目)
    assert result_all_two["He"] == 2  # He (2番目)  # noqa: PLR2004
