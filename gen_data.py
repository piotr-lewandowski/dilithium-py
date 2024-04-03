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

    rounds = 100
    for i in range(rounds):
        msg = random.randbytes(32)
        sig = dilithium.sign(sk, msg)
    
    results = dilithium.leaked_data
    f = open("output", "w")
    for (c, z, y, s1) in results:
        print_results(c, z, y, s1, f)
    f.close()