"""NLP 100 Exercise 2020 Chapter 1: Warm-up
Problem 03: Word Length List
Create a list of the lengths of words in the sentence
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum
mechanics."
"""

import re
from typing import Final


def count_word_lengths(text: str) -> list[int]:
    """Count the number of characters in each word of a text.

    Args:
        text: The input text

    Returns:
        A list of integers representing the length of each word
    """
    # Return an empty list for an empty string
    if not text:
        return []

    # Split the string into words
    words = text.split()

    # Remove punctuation and other symbols from each word and count characters
    lengths = []
    for word in words:
        # Remove punctuation and symbols (keep alphabets, numbers, and Japanese chars)
        clean_word = re.sub(r"[^\w\d\u3000-\u9fff]", "", word)
        # Add the length only if the word is not empty
        if clean_word:
            lengths.append(len(clean_word))

    return lengths


def main() -> None:
    """Main function"""
    text: Final[str] = (
        "Now I need a drink, alcoholic of course, after the heavy lectures involving "
        "quantum mechanics."
    )
    result = count_word_lengths(text)
    print(f"Input: {text}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()
