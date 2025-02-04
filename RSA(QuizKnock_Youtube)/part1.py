
# input
key_num = "23011819"

def number_to_alphabet(key_num):
    # アルファベットのリストを定義(index番号+1がA~Zに対応)
    alphabet = [
        "A", "B", "C", "D", "E", "F", "G",
        "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U",
        "V", "W", "X", "Y", "Z"
    ]

    # 数字の数をチェック(奇数の場合は頭に0を付与)
    if len(key_num) % 2 != 0:
        key_num = key_num.zfill(len(key_num)+1)

    # 2文字ずつ切り取る->アルファベットに変換->リストに格納
    key_word_char = []
    for char_num in range(0, len(key_num), 2):
        slice_start = char_num
        slice_end = slice_start + 2

        char_slice = key_num[slice_start:slice_end]
        append_char = alphabet[int(char_slice)-1]
        key_word_char.append(append_char)

    # リストに格納した文字を結合
    key_word = "".join(key_word_char)
    return key_word

if __name__ == "__main__":
    key_word = number_to_alphabet(key_num)
    print(key_word)
