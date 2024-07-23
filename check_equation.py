from gen_missing_data import run_rounds, setup_logging
from random import Random
from dilithium.dilithium import Dilithium2
from dilithium.utils import reduce_mod_pm

POLYNOMIAL_LENGTH = 256
q = 8380417

def calculate_right_side(j, C, s):
    sum1 = sum(C[i]*s[j - i] for i in range(POLYNOMIAL_LENGTH) if i <= j)
    sum2 = sum(C[i]*s[256 + j - i] for i in range(POLYNOMIAL_LENGTH) if i > j)
    right_side = sum1 - sum2
    return right_side

def print_results(results, logger):
    l = 10
    for (c, z, y, s1) in results:
        logger.info(f"c (ntt): {c[:l]}")
        non_ntt_c = c.copy_from_ntt().from_montgomery()
        logger.info(f"c: {non_ntt_c[:l]}")
        logger.info(f"{sum([1 for i in range(POLYNOMIAL_LENGTH) if non_ntt_c[i] != 0])}")
        logger.info(f"z: {z[0][0][:l]}")
        logger.info(f"y: {y[0][0][:l]}")
        logger.info(f"s1 (ntt): {s1[0][0][:l]}")
        non_ntt_s1 = s1.copy_from_ntt().from_montgomery()
        logger.info(f"s1: {non_ntt_s1[0][0][:l]}")
        logger.info(f"s1.scale(c).from_ntt(): {(s1.scale(c))[0][0].copy_from_ntt().from_montgomery()[:l]}")
        r1 = [calculate_right_side(j, non_ntt_c, non_ntt_s1[0][0]) for j in range(POLYNOMIAL_LENGTH)]
        logger.info(f"r1: {r1[:l]}")
        logger.info(f"r1 + z: {([z[0][0][j] - r1[j] for j in range(POLYNOMIAL_LENGTH)])[:l]}")
    
if __name__ == "__main__":
    rounds = 10
    logger = setup_logging("single")
    random = Random()

    res = run_rounds(rounds, logger, random, Dilithium2)
    print_results(res, logger)