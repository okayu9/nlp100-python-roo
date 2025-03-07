"""NLP 100 Exercise 2020 Chapter 1: Warm-up
Problem 00: Reversing a String
Obtain the string that arranges the characters of the string "stressed" in reverse order (from the end to the beginning).
"""

from typing import Final


def reverse_string(s: str) -> str:
    """Reverse a string.

    Args:
        s: The string to reverse

    Returns:
        The reversed string
    """
    return s[::-1]


def main() -> None:
    """Main function"""
    INPUT: Final[str] = "stressed"
    result = reverse_string(INPUT)
    print(f"Input: {INPUT}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()
