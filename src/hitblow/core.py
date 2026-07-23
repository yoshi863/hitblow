"""ゲームの中心ロジック（純粋関数＝テストしやすい）。

ここは責務「判定と出題」。画面・入力には触らない（それは game.py）。
"""

import random
from collections import Counter


def make_secret(digits=3, allow_duplicates=False):
    """指定された桁数で答えを作る。"""

    numbers = "0123456789"

    if allow_duplicates:
        # 重複あり
        return "".join(
            random.choices(numbers, k=digits)
        )

    # 重複なし
    if digits > 10:
        raise ValueError("重複なしの場合は10桁以下にしてください。")

    return "".join(
        random.sample(numbers, k=digits)
    )


def judge(secret, guess):
    """Hit数とBlow数を求める。重複ありにも対応する。"""

    # 位置と数字の両方が同じ
    hit = sum(
        secret_digit == guess_digit
        for secret_digit, guess_digit in zip(secret, guess)
    )

    # 答えと予想に共通して含まれる数字の個数
    secret_counts = Counter(secret)
    guess_counts = Counter(guess)

    common_count = sum(
        min(secret_counts[digit], guess_counts[digit])
        for digit in secret_counts
    )

    # 共通する数字からHitを除いたものがBlow
    blow = common_count - hit

    return hit, blow
