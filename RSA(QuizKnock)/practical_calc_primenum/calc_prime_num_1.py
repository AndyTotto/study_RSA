import datetime
import math

# input
upper_limit_num = 1000000

def calc_prime_num(upper_limit_num):
    list_prime_num = [2]

    for num in range(3, upper_limit_num+1, 2):
        limit = math.sqrt(num)
        is_prime = True
        for prime_num in list_prime_num:
            if prime_num > limit:
                break
            if num % prime_num == 0:
                is_prime = False
                break
        if is_prime:
            list_prime_num.append(num)
        
    return list_prime_num

if __name__ == "__main__":

    start = datetime.datetime.now()
    list_prime_num = calc_prime_num(upper_limit_num)
    end = datetime.datetime.now()

    with open ("./prime_num_list.txt", "w") as o:
        print(*list_prime_num, sep="\n", file=o)

    # 実行結果出力
    do_time = end - start
    print("実行時間：", do_time)
    print("素数の数：", len(list_prime_num))