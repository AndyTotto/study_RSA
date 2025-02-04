import part1

# input
p = 37
q = 71
e = 79
c = 904

def calc_message(p, q, e, c):
    n = p * q
    phi = (p-1)*(q-1)

    # m(p-1)(q-1)≡-1(mod e)を満たすmを求める
    num = 1
    while True:
        target_num = e * num - 1
        if target_num % phi == 0:
            m = target_num // phi
            print("search complete.")
            break
        num = num + 1
    print("m = ", m)

    # mからdを計算
    d = (m * (p-1) * (q-1) + 1) // e
    print("d = ", d)

    # C,d,nからMを計算
    M = pow(int(c), int(d), int(n))
    print("M = ", M)

    return M

if __name__ == "__main__":
    M = calc_message(p, q, e, c)
    # アルファベットに変換(問題1のアルファベット変換関数を利用)
    word_M = part1.number_to_alphabet(str(M))
    print(word_M)