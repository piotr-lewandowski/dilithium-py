from time import time
from dilithium.dilithium import Dilithium2
from random import Random
from keys import sk
from params import sigma_doubled
from utils import *

class Results:
    def __init__(self, c_lst, z_lst, y_lst, s1_lst):
        self.c_lst = c_lst
        self.z_lst = z_lst
        self.y_lst = y_lst
        self.s1_lst = s1_lst

def run_rounds(rounds, logger, random, dilithium):
    start = time()
    for i in range(rounds):
        if i % 100 == 0:
            logger.info(f"Completed {i}/{rounds} rounds")
        msg = random.randbytes(32)
        dilithium.sign(sk, msg)
    end = time()
    logger.info(f"{rounds} rounds completed in {end - start} s")
    res = dilithium.leaked_data
    dilithium.leaked_data = []
    return res

def parse_results(results):
    parsed = []
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
            s1_lst.append(el[0].copy_from_ntt().from_montgomery().coeffs)
        parsed.append((c_lst, z_lst, y_lst, s1_lst))
    return parsed

def try_append_oracle(m, i, j, file, res, logger):
    (_, _, y_lst, _) = res
    if y_lst[i][j] == 0:
        append(m, i, j, file, res, logger)
        return 1
    return 0

def try_append_heuristic(m, i, j, file, res, logger):
    (_, z_lst, y_lst, _) = res
    if abs(z_lst[i][j]) <= sigma_doubled and y_lst[i][j] != 0:
        append(m, i, j, file, res, logger)
        return 1
    return 0

def run(name: str):
    seed = time().hex() + name
    random = Random(seed)
    dilithium = Dilithium2
    logger = setup_logging(name)

    oracle = "data/oracle.csv"
    heuristic = "data/heuristic.csv"

    initialize_csv(oracle)
    initialize_csv(heuristic)
    max_index = max(find_index(oracle), find_index(heuristic))

    m = max_index + 1
    rounds = 1000
    checked = 0
    found_oracle = 0
    found_heuristic = 0
    try:
        while True:
            raw_res = run_rounds(rounds, logger, random, dilithium)
            checked += rounds
            par_res = parse_results(raw_res)
            i = 0
            for res in par_res:
                for j in range(256):
                    found_oracle += try_append_oracle(m + found_oracle + 1, i, j, oracle, res, logger)
                    found_heuristic += try_append_heuristic(m + found_heuristic + 1, i, j, heuristic, res, logger)
    except KeyboardInterrupt:
        logger.info(f"Checked {checked} rounds")
        logger.info(f"Found {found_oracle} oracle data and {found_heuristic} heuristic data")

if __name__ == "__main__":
    run("console")
