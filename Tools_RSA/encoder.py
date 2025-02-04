import math
import random
import func

# input
message = "test"

def str_to_num(message):

    # アルファベット(大文字・小文字)・記号のリストを定義
    strings_list = func.make_str_list()

    # 1文字ずつ数字(2桁)に変換
    message_num_list = []
    for ch in message:
        char_num = str(strings_list.index(ch)).zfill(2)
        message_num_list.append(char_num)

    message_num = "".join(message_num_list)
    return message_num

def calc_pqe(M):
    # Mを暗号化できる素数p, qを計算する
    M_sqrt = math.sqrt(int(M))
    # Mの桁数までの素数を計算
    loop_limit = 1 * pow(10, len(str(int(M_sqrt))))
    list_prime_num = func.calc_prime_num(loop_limit)
    # Mの平方数~計算した上限までの素数リストからランダムに2つ取り出す->p, q
    candidate_pq = [num for num in list_prime_num if num > M_sqrt]
    p, q = random.sample(candidate_pq, 2)
    # nを計算
    n = p * q
    # (p-1)(q-1)と互いに素となるeを計算
    e = (p-1)*(q-1)-1

    return p, q, n, e

def calc_C(M, n, e):
    C = pow(int(M), e, n)
    return C

if __name__ == "__main__":
    # inputの文字を数字に変換
    M = str_to_num(message)
    # Mを暗号化できる各値を計算
    p, q, n, e = calc_pqe(M)
    # 暗号文Cを計算
    C = calc_C(M, n, e)
    # C, e, n(素数p、qの積)を出力
    print("n =", n)
    print("e =", e)
    print("C =", C)
