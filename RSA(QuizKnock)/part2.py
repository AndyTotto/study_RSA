import part1

# input
p = 37
q = 71
e = 79
c = 904

def calc_message(p, q, e, c):
    n = p * q

    num = 1
    while (True):
        target_num = 79 * num - 1
        #print("target number is " + str(target_num))
        if target_num % 2520 == 0:
            m = target_num / 2520
            print("search complete.")
            break
        num = num + 1

    print("m = ", m)

    d = (m * (p-1) * (q-1) + 1) / e
    print("d = ", d)

    # M = (c ** d) % n
    M = pow(int(c), int(d), int(n))
    print("M = ", M)

    return M

if __name__ == "__main__":
    M = calc_message(p, q, e, c)
    part1.number_to_alphabet(str(M))