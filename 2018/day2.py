from collections import Counter
import numpy as np


def part1(data):
    threes = 0
    twos = 0

    for d in data:
        c = Counter(d)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1

    checksum = twos * threes
    print(checksum)


def part2(data):
    for i, d in enumerate(data):
        for j, e in enumerate(data):
            if i == j:
                continue

            s = np.array(list(map(ord, d)))
            t = np.array(list(map(ord, e)))

            # print(i, j, , len((s-t).nonzero()))
            if (s - t).nonzero()[0].size == 1:
                ind = (s-t).nonzero()[0][0]
                print(d[:ind] + d[ind+1:])


with open("day2.txt") as f:
    data = f.readlines()

    data = [x.strip() for x in data]

part1(data)
part2(data)
