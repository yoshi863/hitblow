"""桁数（難易度）を指定・変更するモジュール"""

def ask_digits(current_digits):
    """
    プレイヤーに桁数を選ばせる関数。
    重複なしの数字は0〜9の10個なので、最大10桁まで指定可能にする。
    """
    print("勇者（プレイヤー）「さあ、世界の平和を守るため、魔王城へ出発だ!」")
    print("勇者が魔王城へ向かっていると、なにかにぶつかってしまった。")
    print("スライム「僕は悪いスライムじゃないよ!」")
    print("スライム「さあ、僕とhit&blowで遊ぼう!」")
    while True:
        ans = input(f"何桁でプレイしますか？（現在の設定: {current_digits}桁）\n変更しない場合はそのままEnter ＞ ").strip()
        
        # Enterだけ押された場合は元の桁数をそのまま返す
        if not ans:
            return current_digits
            
        # 数字かどうか、かつ 1〜10 の範囲内かチェック
        if ans.isdigit():
            keta = int(ans)
            if 1 <= keta <= 10:
                return keta
            else:
                print("※ 1から10の間の数字を入力してね。")
        else:
            print("※ 半角の数字を入力してね。")