import math
import random
import func

# input
message = "test"
# message = "apple"

def str_to_num(message):

    strings_list = func.make_str_list()

    message_num_list = []
    for char_num in range(len(message)):
        slice_start = char_num
        slice_end = slice_start + 1

        char_slice = message[slice_start:slice_end]
        char_num = str(strings_list.index(char_slice)).zfill(2)
        message_num_list.append(char_num)

    message_num = "".join(message_num_list)
    return message_num

def calc_pqe(M):
    M_sqrt = math.sqrt(int(M))
    loop_limit = 1 * pow(10, len(str(int(M_sqrt))))
    list_prime_num = func.calc_prime_num(loop_limit)
    candidate_pq = [num for num in list_prime_num if num > M_sqrt]
    p, q = random.sample(candidate_pq, 2)
    # print(p, q)
    n = p * q
    e = (p-1)*(q-1)-1

    return p, q, n, e

def calc_C(M, n, e):
    C = pow(int(M), e, n)
    return C

if __name__ == "__main__":
    M = str_to_num(message)
    p, q, n, e = calc_pqe(M)
    C = calc_C(M, n, e)
    print(n, e, C)
