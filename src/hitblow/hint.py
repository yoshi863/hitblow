"""10回間違えるごとに表示するヒント機能。"""


def offer_hint(secret, wrong_tries, hint_position):
    """ヒントを表示するか確認し、次のヒント位置を返す。"""

    while True:
        answer = input(
            f"{wrong_tries}回間違えました。"
            "ヒントを表示しますか？"
            "（1：表示する / 2：表示しない）> "
        ).strip()

        if answer == "1":
            if hint_position < len(secret):
                print(
                    f"💡 ヒント：{hint_position + 1}桁目の数字は"
                    f"「{secret[hint_position]}」です"
                )

                # 次回は次の桁をヒントとして表示する
                return hint_position + 1

            print("すべての桁のヒントを表示済みです。")
            return hint_position

        if answer == "2":
            print("ヒントを表示せずにゲームを続けます。")
            return hint_position

        print("1 または 2 を入力してください。")