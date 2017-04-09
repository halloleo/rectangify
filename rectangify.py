import csv

marker = "---"

with open('data.txt', 'r') as inpfile:
    lines = inpfile.read().splitlines()

if lines[0] != marker:
    lines.insert(0, marker)

# distribute to columns
cols = []
for l in lines:
    if l == marker:
        print ("New col!!!")
        cols.append([])
        continue

    col = cols[-1]
    col.append(l)

print (cols)

# output columns
with open('eggs.csv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    row = 0
    while True:
        line_added = False
        out = []
        for col in cols:
            val = ""
            if row < len(col):
                val = col[row]
                line_added = True
            out.append(val)
        if not line_added:
            break
        csvwriter.writerow(out)
        row += 1


