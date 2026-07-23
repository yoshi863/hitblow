"""コマンドの入口。第3回で `hitblow` コマンドがここ（main）を呼ぶ。"""

import random
from collections.abc import Sequence


def make_answer(digits: int = 3) -> list[int]:
    """重複しない正解の数字を作成する。"""
    return random.sample(range(10), digits)


def judge(
    answer: Sequence[int],
    guess: Sequence[int],
) -> tuple[int, int]:
    """Hit数とBlow数を計算する。"""
    hit = sum(
        answer_digit == guess_digit
        for answer_digit, guess_digit in zip(answer, guess)
    )

    blow = sum(digit in answer for digit in guess) - hit

    return hit, blow


def offer_hint(
    answer: Sequence[int],
    revealed_positions: set[int],
) -> None:
    """プレイヤーにヒントを見るか確認する。"""

    while True:
        choice = input("ヒントを表示しますか？ [y/n]: ").strip().lower()

        if choice in ("y", "yes", "はい"):
            break

        if choice in ("n", "no", "いいえ"):
            print("ヒントを使用せず、ゲームを続けます。")
            return

        print("y または n を入力してください。")

    unrevealed_positions = [
        position
        for position in range(len(answer))
        if position not in revealed_positions
    ]

    if not unrevealed_positions:
        print("表示できるヒントはすべて使用済みです。")
        return

    position = unrevealed_positions[0]
    revealed_positions.add(position)

    print(
        f"ヒント：{position + 1}桁目の数字は "
        f"{answer[position]} です。"
    )


def main() -> None:
    digits = 3
    answer = make_answer(digits)

    mistake_count = 0
    revealed_positions: set[int] = set()

    print("Hit & Blowを開始します。")
    print(f"重複しない{digits}桁の数字を当ててください。")

    while True:
        text = input(f"{digits}桁の数字を入力してください：").strip()

        # 不正な入力は間違い回数に含めない
        if not text.isdigit():
            print("数字だけを入力してください。")
            continue

        if len(text) != digits:
            print(f"{digits}桁で入力してください。")
            continue

        if len(set(text)) != digits:
            print("同じ数字を重複して使用しないでください。")
            continue

        guess = [int(number) for number in text]

        hit, blow = judge(answer, guess)
        print(f"Hit: {hit}, Blow: {blow}")

        if hit == digits:
            print(
                f"正解です！ "
                f"{mistake_count + 1}回目の回答で正解しました。"
            )
            break

        mistake_count += 1
        print(f"間違い回数: {mistake_count}")

        if mistake_count % 10 == 0:
            print(f"\n{mistake_count}回間違えました。")
            offer_hint(answer, revealed_positions)


if __name__ == "__main__":
    main()