"""NLP 100 Exercise 2020 Chapter 1: Warm-up
Problem 04: Element Symbol Map
Create a dictionary mapping from the first one or two letters of each word to its
position in the sentence "Hi He Lied Because Boron Could Not Oxidize Fluorine. New
Nations Might Also Sign Peace Security Clause. Arthur King Can."
For words at positions 1, 5, 6, 7, 8, 9, 15, 16, 19, take the first letter.
For all other words, take the first two letters.
"""

import re
from typing import Final


def create_element_map(
    text: str, one_char_positions: set[int] | None = None
) -> dict[str, int]:
    """Create a dictionary mapping from element symbols to their positions.

    For words at positions specified in one_char_positions (1-indexed),
    take the first letter as the key.
    For all other words, take the first two letters as the key.
    The value is the position of the word (1-indexed).

    Args:
        text: The input text
        one_char_positions: Set of positions (1-indexed) where only the first letter
            should be taken. Default is {1, 5, 6, 7, 8, 9, 15, 16, 19}.

    Returns:
        A dictionary mapping from element symbols to their positions
    """
    # Set default value
    if one_char_positions is None:
        one_char_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}

    # Return an empty dictionary for an empty string
    if not text:
        return {}

    # Split the string into words
    words = text.split()

    # Create the dictionary
    element_map = {}
    for i, word in enumerate(words, 1):
        # Remove punctuation and other symbols
        clean_word = re.sub(r"[^\w\d\u3000-\u9fff]", "", word)

        # Process only if the word is not empty
        if clean_word:
            # Get 1 or 2 characters based on the position
            if i in one_char_positions:
                symbol = clean_word[0]
            else:
                # Take only 1 character if the word has only 1 character
                symbol = clean_word[: min(2, len(clean_word))]

            # Add to the dictionary
            element_map[symbol] = i

    return element_map


def main() -> None:
    """Main function"""
    text: Final[str] = (
        "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might "
        "Also Sign Peace Security Clause. Arthur King Can."
    )
    # Take first letter for words at positions 1, 5, 6, 7, 8, 9, 15, 16, 19 as specified
    one_char_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}
    result = create_element_map(text, one_char_positions)
    print(f"Input: {text}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()
