from dilithium import Dilithium2
from random import Random

# c is a polynomial, z and y are 4x1 matrices of polynomials
# prints the coefficients as 256-element arrays
def print_results(c, z, y, s1):
    print("c=")
    print(c.copy_from_ntt().coeffs)
    print("z=")
    for row in z:
        print(row[0].coeffs)
    print("y=")
    for row in y:
        print(row[0].coeffs)
    print("s1=")
    for row in s1:
        print(row[0].coeffs)


if __name__ == "__main__":
    random = Random()
    dilithium = Dilithium2
    pk, sk = dilithium.keygen()

    rounds = 10
    for i in range(rounds):
        msg = random.randbytes(32)
        sig = dilithium.sign(sk, msg)
    
    results = dilithium.leaked_data
    for (c, z, y, s1) in results:
        print_results(c, z, y, s1)