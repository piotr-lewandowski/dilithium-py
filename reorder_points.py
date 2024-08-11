from sys import argv

dataset = argv[1]

file = f"data/{dataset}.csv"

new = []
i = 0
header = ""

with open(file, "r") as csv_file:
    header = csv_file.readline()
    for line in csv_file.readlines():
        i += 1
        rest = line.split(",")[1:]
        j = int(line.split(",")[2])
        new.append((j, str(i) + "," + ",".join(rest)))

new = [x[1] for x in sorted(new, key=lambda x: x[0])]

with open(file, "w") as csv_file:
    csv_file.writelines([header])
    csv_file.writelines(new)