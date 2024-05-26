import regex as re


regex = re.compile(r".*,( .*),.*,.*, \[.*\],.*")
ls = [0, 0, 0, 0]

with open('final_cut.csv', 'w') as outfile:
    with open("final.csv") as infile:
        for line in infile:
            mo = regex.search(line)
            if mo is None:
                continue
            i = mo.group(1)
            if ls[int(i)] == 256:
                continue
            ls[int(i)] += 1
            outfile.writelines(line)
print(ls)
