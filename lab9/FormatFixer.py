# Author : John Patrick Pitts
# Date   : June 28, 2021
# File   : FormatFixer.py


with open("lab9data.txt", "r") as f:
    data = []
    for line in f.readlines():
        print(line)
        row = line.strip().split(",")
        row[0] += row[2]
        row[1] = str(int(row[1]) * 100)+"\n"
        data.append(", ".join(row[:2]))

    newfile = open("data_fixed.txt", "w")
    newfile.writelines(data)
    newfile.close()

# with open("data_fixed.txt", "r") as f:
#     for line in f.readlines():
#         print(line)

