"""NLP 100 Exercise 2020 Chapter 1: Warm-up
Problem 01: Extracting Odd-Positioned Characters
Extract characters at odd positions (1st, 3rd, 5th, ...) from a given string.
"""

from typing import Final


def extract_odd_chars(s: str) -> str:
    """Extract characters at odd positions (1st, 3rd, 5th, ...) from a string.

    Args:
        s: The input string

    Returns:
        A string containing only characters at odd positions
    """
    return s[::2]


def main() -> None:
    """Main function"""
    input_str: Final[str] = "パタトクカシーー"
    result = extract_odd_chars(input_str)
    print(f"Input: {input_str}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()
