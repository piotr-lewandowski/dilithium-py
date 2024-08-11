from os import system
from shutil import copyfile

# run command in shell
datasets = [ "mixed_1"]
models = ["base"]

for dataset in datasets:
    system(f"python3 ./reorder_points.py {dataset}")
    system(f"python3 ./csv_to_ampl/generate_ampl.py {dataset}")
    copyfile(f"./csv_to_ampl/{dataset}.dat", f"./ampl/data/dat.dat")
    for model in models:
        copyfile(f"./ampl/models/{model}.mod", f"./ampl/models/mod.mod")
        system(f"ampl -t ./ampl/run.run")
