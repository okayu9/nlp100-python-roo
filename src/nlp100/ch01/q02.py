"""NLP 100 Exercise 2020 Chapter 1: Warm-up
Problem 02: Alternating Characters
Obtain the string "パタトクカシーー" by concatenating the characters at
alternating positions from the strings "パトカー" and "タクシー".
"""

from typing import Final


def alternate_concat(s1: str, s2: str) -> str:
    """Concatenate characters from two strings alternately.

    Args:
        s1: The first string
        s2: The second string

    Returns:
        A string with characters from s1 and s2 alternately
    """
    result = ""
    # Concatenate alternately up to the length of the shorter string
    for i in range(min(len(s1), len(s2))):
        result += s1[i] + s2[i]

    # Add the remaining characters from the longer string
    if len(s1) > len(s2):
        result += s1[len(s2) :]
    elif len(s2) > len(s1):
        result += s2[len(s1) :]

    return result


def main() -> None:
    """Main function"""
    str1: Final[str] = "パトカー"
    str2: Final[str] = "タクシー"
    result = alternate_concat(str1, str2)
    print(f"Input 1: {str1}")
    print(f"Input 2: {str2}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()
