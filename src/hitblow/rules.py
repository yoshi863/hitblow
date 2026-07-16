def ask_allow_duplicates() -> bool:
    """数字の重複を許可するか入力してもらう。"""

    while True:
        answer = input("数字の重複を許可しますか？（y/n）: ").strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("y または n を入力してください。")