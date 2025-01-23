import datetime
import math

# input
upper_limit_num = 10

def calc_prime_num(upper_limit_num):
    # 2は素数のため追加
    list_prime_num = [2]

    # 3から順番に確認
    for num in range(3, upper_limit_num+1, 2):
        # 最大数の平方数まで確認すればOK
        limit = math.sqrt(num)
        is_prime = True
        # 確認した数までの素数で割れるか確認
        for prime_num in list_prime_num:
            # 必要ループ数以上で終了
            if prime_num > limit:
                break
            # 割り切れたら素数では無い。次の数へ
            if num % prime_num == 0:
                is_prime = False
                break
        # 割り切れなかったら新しく素数に追加
        if is_prime:
            list_prime_num.append(num)
        
    return list_prime_num

if __name__ == "__main__":

    start = datetime.datetime.now()
    list_prime_num = calc_prime_num(upper_limit_num)
    end = datetime.datetime.now()

    # 求めた素数をカレントディレクトリに出力
    with open ("./prime_num_list.txt", "w") as o:
        print(*list_prime_num, sep="\n", file=o)

    # 実行結果出力
    do_time = end - start
    print("実行時間：", do_time)
    print("素数の数：", len(list_prime_num))