import math
import func

# input
n = 32859391
e = 32847911
C = 16854072

# nからp, qを計算
def calc_pq(n):
    num_limit = int(math.sqrt(n))
    list_prime_num = func.calc_prime_num(num_limit)
    for num in list_prime_num:
        if n % num == 0:
            p = num
            break
    q = n // p
    return p, q

# Mを計算
def calc_M(p, q, n, e, C):
    if n != p * q:
        print("error")
        return None

    '''
    num_x = 1 #これはブログに残したい
    while True:
        target_num = e * num_x - 1
        if target_num % phi == 0:
            m = target_num // phi
            break
        num_x = num_x + 1
    '''

    # mを計算(dの計算に必要)
    phi_n = (p-1)*(q-1)
    inverse_phi = pow(phi_n, -1, e)
    m = ((e-1)*inverse_phi) % e
    # dを計算
    d = (m*(p-1)*(q-1) + 1) // e
    # d, C, nからMを計算
    M = pow(C, d, n)
    
    return M

# Mから元のメッセージを復元
def num_to_str(M):
    M = str(M)
    # アルファベット・記号のリストを定義
    strings_list = func.make_str_list()

    # 桁数が奇数の時、頭に0を付けて偶数にする
    if len(M) % 2 != 0:
        M = M.zfill(len(M)+1)
    
    # 2桁ずつ切り出して文字に変換->リスト
    message_list = []
    for char_num in range(0, len(M), 2):
        char_slice = M[char_num:char_num+2]
        char = strings_list[int(char_slice)]
        message_list.append(char)
    # リストを結合してメッセージに
    message = "".join(message_list)

    return message

if __name__ == "__main__":
    # nからp, qを計算
    p, q = calc_pq(n)
    # Mを計算
    M = calc_M(p, q, n, e, C)
    # Mから元のメッセージを復元
    message = num_to_str(M)

    print("message = ", message)