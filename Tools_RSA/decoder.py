import math
import func

# input
n = 74985217
e = 74967855
C = 40593472

def calc_pq(n):
    num_limit = int(math.sqrt(n))
    list_prime_num = func.calc_prime_num(num_limit)
    for num in list_prime_num:
        if n % num == 0:
            p = num
            break
    q = n // p
    return p, q

def calc_M(p, q, n, e, C):
    if n != p * q:
        print("error")
    m = 1
    while(True):
        if m*(p-1)*(q-1) % e == e-1:
            break
        m = m + 1
    d = (m*(p-1)*(q-1) + 1) // e
    M = pow(C, d, n)
    
    return M

def num_to_str(M):
    M = str(M)
    strings_list = func.make_str_list()
    print(len(M))

    if len(M) % 2 != 0:
        M = M.zfill(len(M)+1)
    
    print(M)

    message_list = []
    for char_num in range(len(M)//2):
        slice_start = char_num*2
        slice_end = slice_start + 2

        char_slice = M[slice_start:slice_end]

        char = strings_list[int(char_slice)]
        message_list.append(char)
    message = "".join(message_list)

    return message

if __name__ == "__main__":
    p, q = calc_pq(n)
    M = calc_M(p, q, n, e, C)
    message = num_to_str(M)

    print("message = ", message)