import math

# input
target_num = 177773

def define_upper_limit_num(target_num):
    upper_limit_num = int(math.sqrt(target_num))
    print(upper_limit_num)
    return upper_limit_num

def calc_prime_num(upper_limit_num):
    list_prime_num = [2]
    print(len(list_prime_num))

    for num in range(3, upper_limit_num+1):
        count = 1
        for prime_num in list_prime_num:
            if num % prime_num == 0:
                break
            if count == len(list_prime_num):
                # print("add prime num = ", num)
                list_prime_num.append(num)
            count = count + 1
        
    return list_prime_num

def factorization(target_num, list_prime_num):
    for num in list_prime_num:
        if target_num % num == 0:
           print(num, target_num / num)
           break

if __name__ == "__main__":
    upper_limit_num = define_upper_limit_num(target_num)
    list_prime_num = calc_prime_num(upper_limit_num)
    factorization(target_num, list_prime_num)
        