import datetime

# input
upper_limit_num = 10

def calc_eratosthenes(upper_limit_num):

    # 上限の平方数まで確認すればOK
    loop_limit = upper_limit_num ** 0.5
    # 上限数のTrueリストを生成、indexを数で管理する
    list_sieve = [True] * (upper_limit_num + 1)

    # 0、1は素数ではないためFalse
    list_sieve[0] = False
    list_sieve[1] = False

    # 2~上限の平方数までを確認
    target_num = 2
    while target_num < loop_limit:
        # 素数(=True)の場合 → 倍数をFalseに
        if list_sieve[target_num] == True:
            for num in range(target_num*target_num, len(list_sieve), target_num):
                list_sieve[num] = False
        target_num = target_num + 1

    # Trueで残った数のみリストで出力
    list_prime_num = [index for index, flag in enumerate(list_sieve) if flag == True]
    return list_prime_num

if __name__ == "__main__":
    start = datetime.datetime.now()
    list_prime_num = calc_eratosthenes(upper_limit_num)
    end = datetime.datetime.now()

    # 求めた素数をカレントディレクトリに出力
    with open ("./prime_num_list.txt", "w") as o:
        print(*list_prime_num, sep="\n", file=o)

    # 実行結果出力
    do_time = end - start
    print("実行時間：", do_time)
    print("素数の数：", len(list_prime_num))
