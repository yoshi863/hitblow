"""ゲームの中心ロジック（純粋関数＝テストしやすい）。

ここは責務「判定と出題」。画面・入力には触らない（それは game.py）。
"""

import random
from collections import Counter


def judge(secret: str, guess: str) -> tuple[int, int]:
    """Hit数とBlow数を返す。重複する数字にも対応する。"""

    hit = sum(
        secret_digit == guess_digit
        for secret_digit, guess_digit in zip(secret, guess)
    )

    secret_counts = Counter(secret)
    guess_counts = Counter(guess)

    total_matches = sum(
        min(secret_counts[number], guess_counts[number])
        for number in secret_counts
    )

    blow = total_matches - hit

    return hit, blow


def make_secret(
    digits: int = 3,
    allow_duplicates: bool = False,
) -> str:
    """指定された桁数と重複設定で秘密の数字を作る。"""

    if digits < 1:
        raise ValueError("桁数は1以上にしてください")

    if not allow_duplicates and digits > 10:
        raise ValueError("重複なしの場合、桁数は10以下にしてください")

    numbers = "0123456789"

    if allow_duplicates:
        # 同じ数字が複数回選ばれる可能性がある
        return "".join(random.choices(numbers, k=digits))

    # 同じ数字を使わずに選ぶ
    return "".join(random.sample(numbers, k=digits))