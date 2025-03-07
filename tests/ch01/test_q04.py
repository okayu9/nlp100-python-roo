"""Tests for NLP 100 Exercise Chapter 1 Problem 04."""

from nlp100.ch01.q04 import create_element_map


def test_create_element_map() -> None:
    """Test for create_element_map function."""
    # When the string is empty
    assert create_element_map("") == {}

    # When there is only one word (take the first character for the 1st word)
    assert create_element_map("Hello", {1}) == {"H": 1}

    # When there are multiple words (1st word takes 1 character, others take 2)
    assert create_element_map("Hi World", {1}) == {"H": 1, "Wo": 2}

    # Example from the problem statement
    text = (
        "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might "
        "Also Sign Peace Security Clause. Arthur King Can."
    )
    one_char_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}
    result = create_element_map(text, one_char_positions)

    # Words at positions 1, 5, 6, 7, 8, 9, 15, 16, 19 take the first character
    assert result["H"] == 1  # Hi (1st)
    assert result["B"] == 5  # Boron (5th)  # noqa: PLR2004
    assert result["C"] == 6  # Could (6th)  # noqa: PLR2004
    assert result["N"] == 7  # Not (7th)  # noqa: PLR2004
    assert result["O"] == 8  # Oxidize (8th)  # noqa: PLR2004
    assert result["F"] == 9  # Fluorine. (9th)  # noqa: PLR2004
    assert result["P"] == 15  # Peace (15th)  # noqa: PLR2004
    assert result["S"] == 16  # Security (16th)  # noqa: PLR2004
    assert result["K"] == 19  # King (19th)  # noqa: PLR2004

    # All other words take the first two characters
    assert result["He"] == 2  # He (2nd)  # noqa: PLR2004
    assert result["Li"] == 3  # Lied (3rd)  # noqa: PLR2004
    assert result["Be"] == 4  # Because (4th)  # noqa: PLR2004
    assert result["Ne"] == 10  # New (10th)  # noqa: PLR2004
    assert result["Na"] == 11  # Nations (11th)  # noqa: PLR2004
    assert result["Mi"] == 12  # Might (12th)  # noqa: PLR2004
    assert result["Al"] == 13  # Also (13th)  # noqa: PLR2004
    assert result["Si"] == 14  # Sign (14th)  # noqa: PLR2004
    assert result["Cl"] == 17  # Clause. (17th)  # noqa: PLR2004
    assert result["Ar"] == 18  # Arthur (18th)  # noqa: PLR2004
    assert result["Ca"] == 20  # Can. (20th)  # noqa: PLR2004

    # Test with different patterns
    # When taking the first character of all words
    all_positions = set(range(1, 21))
    result_all_one = create_element_map(text, all_positions)
    assert result_all_one["H"] == 2  # noqa: PLR2004  # He (2nd) - overwritten due to duplication
    assert result_all_one["H"] != 1  # Hi (1st) - overwritten due to duplication

    # When taking the first two characters of all words
    result_all_two = create_element_map(text, set())
    assert result_all_two["Hi"] == 1  # Hi (1st)
    assert result_all_two["He"] == 2  # He (2nd)  # noqa: PLR2004
