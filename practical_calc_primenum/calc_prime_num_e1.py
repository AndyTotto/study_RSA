import datetime

# input
upper_limit_num = 1000000
loop_limit = upper_limit_num ** 0.5

def calc_prime_num(upper_limit_num):
    list_prime_num = []
    for input_num in range(2, upper_limit_num+1):
        list_prime_num.append(input_num)

    list_prime_num = calc_eratosthenes(list_prime_num)

    return list_prime_num

def calc_eratosthenes(list_prime_num):

    target_index = 0
    while True:
        target_num = list_prime_num[target_index]
        if list_prime_num[target_index] > loop_limit:
            return list_prime_num
        
        list_prime_num = [num for num in list_prime_num if num == target_num or num % target_num != 0]
        target_index = target_index + 1
            

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
