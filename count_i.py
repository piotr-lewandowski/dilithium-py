import regex as re


# Creating a list of filenames
filenames = ["wynik1.csv", "wynik2.csv", "wynik3.csv",
             "wynik4.csv", "wynik5.csv", "wynik6.csv"]

# Open file3 in write mode
with open('final.csv', 'w') as outfile:

    # Iterate through list
    for names in filenames:

        # Open each file in read mode
        with open(names) as infile:

            # read the data from file1 and
            # file2 and write it in file3
            outfile.write(infile.read())

        # Add '\n' to enter data of file2
        # from next line
        outfile.write("\n")

regex = re.compile(r".*,( .*),.*,.*, \[.*\],.*")
ls = [0, 0, 0, 0]

with open("final.csv", 'r') as file:
    for line in file:
        mo = regex.search(line)
        if mo is None:
            continue
        i = mo.group(1)
        ls[int(i)] += 1

print(ls)
