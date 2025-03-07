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
    # デフォルト値の設定
    if one_char_positions is None:
        one_char_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}

    # 空文字列の場合は空辞書を返す
    if not text:
        return {}

    # 文字列を単語に分割
    words = text.split()

    # 辞書の作成
    element_map = {}
    for i, word in enumerate(words, 1):
        # 句読点などの記号を取り除く
        clean_word = re.sub(r"[^\w\d\u3000-\u9fff]", "", word)

        # 空でない場合のみ処理
        if clean_word:
            # 位置に応じて1文字または2文字を取得
            if i in one_char_positions:
                symbol = clean_word[0]
            else:
                # 単語が1文字しかない場合は1文字だけ取る
                symbol = clean_word[: min(2, len(clean_word))]

            # 辞書に追加
            element_map[symbol] = i

    return element_map


def main() -> None:
    """Main function"""
    text: Final[str] = (
        "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might "
        "Also Sign Peace Security Clause. Arthur King Can."
    )
    # 問題の指定通り、1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字を取る
    one_char_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}
    result = create_element_map(text, one_char_positions)
    print(f"Input: {text}")
    print(f"Output: {result}")


if __name__ == "__main__":
    main()
