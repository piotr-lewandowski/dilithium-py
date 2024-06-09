from time import time
from dilithium import Dilithium2
from random import Random
from sk import sk
from pk import pk

# c is a polynomial, z and y are 4x1 matrices of polynomials
# prints the coefficients as 256-element arrays

random = Random()
dilithium = Dilithium2
# pk, sk = dilithium.keygen()

with open("wynik1.csv", "a") as csv_file:
    m = 0
    rounds = 6500
    # rounds = 100000
    # rounds = 1000
    # rounds = 10000
    start = time()
    for i in range(rounds):
        # print(i)
        if i % 1000 == 0:
            print(i // 1000)
        msg = random.randbytes(32)
        sig = dilithium.sign(sk, msg)
    results = dilithium.leaked_data
    all = []
    for (c, z, y, s1) in results:
        c_lst = c.copy_from_ntt().from_montgomery().coeffs
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
                if y_lst[i][j] == 0:
                    m += 1
                    csv_file.writelines(f"{m}, {i}, {j}, {z_lst[i][j]}, {c_lst}, {s1_lst[i][j]}\n")
    end = time()
    print(end - start)
