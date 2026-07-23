"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret
from .keta import ask_digits


def ask_duplicates():
    """数字の重複を許可するかプレイヤーに聞く。"""
    while True:
        answer = input(
            "数字の重複を選んでください（1：重複なし / 2：重複あり）> "
        ).strip()

        if answer == "1":
            return False

        if answer == "2":
            return True

        print("1 または 2 を入力してください。")


def play(digits=3):
    # ===== ① ゲーム開始時の設定 =====

    # プレイヤーに桁数を聞く
    digits = ask_digits(digits)

    # プレイヤーに重複の有無を聞く
    allow_duplicates = ask_duplicates()

    # 選択されたルールで答えを作る
    secret = make_secret(
        digits,
        allow_duplicates=allow_duplicates,
    )

    duplicate_text = "あり" if allow_duplicates else "なし"

    print()
    print(f"Hit & Blow（{digits}桁・重複{duplicate_text}）")
    print(f"👉 {digits} 桁でゲームをスタートします！")

    tries = 0

    while True:
        guess = input("予想 > ").strip()

        # ===== ② 入力コマンドに足す（ヒントなど） =====
        # 例：
        # from .hint import hint
        # if guess == "h":
        #     print(hint(secret))
        #     continue

        # 数字と桁数を確認
        if len(guess) != digits or not guess.isdigit():
            print(f"{digits}桁の数字で入力してね")
            continue

        # 重複なしルールの場合、同じ数字がないか確認
        if not allow_duplicates and len(set(guess)) != digits:
            print("重複なしルールです。同じ数字は使わないでね")
        

        tries += 1

        hit, blow = judge(secret, guess)

        print(f"  Hit={hit}  Blow={blow}")

        if hit == digits:
            # ===== ③ 勝利時に足す（スコア・履歴など） =====

            print(f"正解！ {tries}回で当たり（答え {secret}）")
            break