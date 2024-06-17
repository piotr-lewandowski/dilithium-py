from concurrent.futures import *
from gen_missing_data import *

executor = ThreadPoolExecutor(max_workers=6)

while True:
    names = [f"run_{i}" for i in range(6)]

    futures = { executor.submit(run, name) : name for name in names }

    for future in as_completed(futures):
        name = futures[future]
        try:
            left = future.result()
            print(f"{name} finished successfully, there are {left} datapoints left")
        except Exception as exc:
            print('%s generated an exception: %s' % (name, exc))
        