"""NLP 100 Exercise 2020 Chapter 1: Warm-up
Problem 03: Word Length List
Create a list of the lengths of words in the sentence
"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
"""

import re
from typing import Final, List


def count_word_lengths(text: str) -> List[int]:
    """Count the number of characters in each word of a text.

    Args:
        text: The input text

    Returns:
        A list of integers representing the length of each word
    """
    # 空文字列の場合は空リストを返す
    if not text:
        return []

    # 文字列を単語に分割
    words = text.split()

    # 各単語から句読点などの記号を取り除き、文字数をカウント
    lengths = []
    for word in words:
        # 句読点などの記号を取り除く（アルファベット、数字、日本語文字以外を削除）
        clean_word = re.sub(r"[^\w\d\u3000-\u9fff]", "", word)
        # 空でない場合のみ文字数を追加
        if clean_word:
            lengths.append(len(clean_word))

    return lengths


def main() -> None:
    """Main function"""
    text: Final[str] = (
        "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    )
    result = count_word_lengths(text)
    print(f"Input: {text}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()
