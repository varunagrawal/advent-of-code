def part1(rows):
    sum = 0
    for row in rows:
        sum += (max(row) - min(row))

    return sum

def part2(rows):
    sum = 0
    for row in rows:
        for i in range(len(row)):
            for j in range(len(row)):
                if i != j and row[j] % row[i] == 0:
                    sum += (row[j] // row[i])
                    break
    return sum


with open("day2.in", 'r') as f:
    inp = f.readlines()

rows = []
for l in inp:
    rows.append([int(x) for x in l.split('\t')])

print(part1(rows))
print(part2(rows))
