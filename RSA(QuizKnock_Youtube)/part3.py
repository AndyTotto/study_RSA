import math

# input
target_num = 177773

def calc_pq(n):
    # 2~target_numの平方数までに必ず約数が1つある
    num_limit = int(math.sqrt(n))
    # target_numの平方数までの素数を計算→リスト
    list_prime_num = calc_prime_num(num_limit)
    # 素数リストから該当の約数を探す
    for num in list_prime_num:
        if n % num == 0:
            p = num
            break
    q = n // p
    return p, q

# エラトステネスのふるい
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

if __name__ == "__main__":
    p, q = calc_pq(target_num)
    print("p=", p)
    print("q=", q)
