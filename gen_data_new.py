from dilithium import Dilithium2
from random import Random

# c is a polynomial, z and y are 4x1 matrices of polynomials
# prints the coefficients as 256-element arrays


def print_results(c, z, y, s1, f):
    f.write("c=\n")
    f.write(str(c.copy_from_ntt().coeffs))
    f.write("\n")
    f.write("z=\n")
    for row in z:
        f.write(str(row[0].coeffs))
        f.write("\n")
    f.write("y=\n")
    for row in y:
        f.write(str(row[0].coeffs))
        f.write("\n")
    f.write("s1=\n")
    for row in s1:
        f.write(str(row[0].coeffs))
        f.write("\n")


if __name__ == "__main__":
    random = Random()
    dilithium = Dilithium2
    pk, sk = dilithium.keygen()

    rounds = 2
    # rounds = 100000
    for i in range(rounds):
        print(i)
        if i % 1000 == 0:
            print(i // 1000)
        msg = random.randbytes(32)
        sig = dilithium.sign(sk, msg)

    results = dilithium.leaked_data
    all = []
    for (c, z, y, s1) in results:
        c_lst = c.copy_from_ntt().coeffs
        z_lst = []
        y_lst = []
        s1_lst = []
        for el in z:
            z_lst.append(el[0].coeffs)
        for el in y:
            y_lst.append(el[0].coeffs)
        for el in s1:
            s1_lst.append(el[0].coeffs)
        for i in range(len(z_lst)):
            for j in range(len(z_lst[0])):
                # if y_lst[i][j] % 2 == 0:
                # if y_lst[i][j] == 0:
                if True:
                    all.append([c_lst, z_lst, y_lst, s1_lst])
                    break
    with open("proba.txt", "w") as k:
        k.write(str(all))
    # with open("to.txt", "w") as f:
    #     # a = []
    #     # for (c, z, y, s1) in results:
    #     #     a.append(y)
    #     for (c, z, y, s1) in results:
    #         print_results(c, z, y, s1, f)
    #         # for i in y:
    #         # # if any(list(map((lambda x: x == 0), y[0][0].coeffs))):
    #         #     print(i[0].coeffs)
