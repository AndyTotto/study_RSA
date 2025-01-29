def make_str_list():
    strings_list = [
        " ",

        "a", "b", "c", "d", "e", "f", "g",
        "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t", "u",
        "v", "w", "x", "y", "z",

        "A", "B", "C", "D", "E", "F", "G",
        "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T", "U",
        "V", "W", "X", "Y", "Z",

        "-", "'", "!", "?", "."
    ]

    return strings_list


def calc_prime_num(input_num):

    # 上限の平方数まで確認すればOK
    loop_limit = input_num ** 0.5
    # 上限数のTrueリストを生成、indexを数で管理する
    list_sieve = [True] * (input_num + 1)

    # 0、1は素数ではないためFalse
    list_sieve[0] = False
    list_sieve[1] = False

    # 2~上限の平方数までを確認
    target_num = 2
    while target_num < loop_limit:
        # 素数(=True)の場合 → 倍数をFalseに
        if list_sieve[target_num]:
            for num in range(target_num*target_num, len(list_sieve), target_num):
                list_sieve[num] = False
        target_num = target_num + 1

    # Trueで残った数のみリストで出力
    list_prime_num = [index for index, flag in enumerate(list_sieve) if flag == True]
    return list_prime_num