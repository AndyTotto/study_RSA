import math
import func

# input
n = 3283716497
e = 3283583855
C = 2827144907

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
        return None
    '''
    m = 1 #これはブログに残したい
    while True:
        if m*(p-1)*(q-1) % e == e-1:
            break
        m = m + 1
    '''
    phi_n = (p-1)*(q-1)
    inverse_phi = pow(phi_n, -1, e)
    m = ((e-1)*inverse_phi) % e
    d = (m*(p-1)*(q-1) + 1) // e
    M = pow(C, d, n)
    
    return M

def num_to_str(M):
    M = str(M)
    strings_list = func.make_str_list()

    if len(M) % 2 != 0:
        M = M.zfill(len(M)+1)
    
    message_list = []
    for char_num in range(0, len(M), 2):
        char_slice = M[char_num:char_num+2]
        char = strings_list[int(char_slice)]
        message_list.append(char)
    message = "".join(message_list)

    return message

if __name__ == "__main__":
    p, q = calc_pq(n)
    M = calc_M(p, q, n, e, C)
    message = num_to_str(M)

    print("message = ", message)