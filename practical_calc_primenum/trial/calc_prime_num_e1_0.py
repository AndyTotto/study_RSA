import datetime

# input
upper_limit_num = 1000000

def calc_eratosthenes(upper_limit_num):

    loop_limit = upper_limit_num ** 0.5
    list_sieve = [True] * (upper_limit_num + 1)

    list_sieve[0] = False
    list_sieve[1] = False

    target_num = 2
    while True:
        if target_num > loop_limit:
            break
        if list_sieve[target_num] == False:
            target_num = target_num + 1
            continue
        if list_sieve[target_num] == True:
            for num in range(target_num*2, len(list_sieve), target_num):
                list_sieve[num] = False
        
        target_num = target_num + 1

    list_prime_num = [index for index, flag in enumerate(list_sieve) if flag == True]
    return list_prime_num

if __name__ == "__main__":
    start = datetime.datetime.now()
    list_prime_num = calc_eratosthenes(upper_limit_num)
    end = datetime.datetime.now()

    with open ("./prime_num_list.txt", "w") as o:
        print(*list_prime_num, sep="\n", file=o)

    # 実行結果出力
    do_time = end - start
    print("実行時間：", do_time)
    print("素数の数：", len(list_prime_num))
