import numpy as np
from itertools import cycle, accumulate


def part1(filename):
    with open(filename) as f:
        data = f.readlines()

    data = np.asarray(list(map(int, data)))
    print(data.sum())


def part2(filename):
    with open(filename) as f:
        data = f.readlines()
    data = list(map(int, data))

    # freq = 0
    # freq_list = [0, ]
    # ptr = 0
    # while True:
    #     freq = freq + data[ptr]
    #     if freq in freq_list:
    #         print("Repeated frequency:", freq)
    #         # break
    #         exit(0)
    #     else:
    #         freq_list.append(freq)

    #     ptr = (ptr + 1) % len(data)
    #     # print(ptr, freq)

    # this is a faster solution using optimized itertools
    seen = set()
    print(next(f for f in accumulate(cycle(data)) if f in seen or seen.add(f)))


part1("day1_1.txt")
part2("day1_1.txt")
