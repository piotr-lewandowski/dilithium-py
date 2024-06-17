
file = "data/everything.csv"

new = []
i = 2500
header = ""

with open(file, "r") as csv_file:
    header = csv_file.readline()
    for line in csv_file.readlines():
        i += 1
        rest = line.split(",")[1:]
        new.append(str(i) + "," + ",".join(rest))

with open(file, "w") as csv_file:
    csv_file.writelines([header])
    csv_file.writelines(new)