import numpy as np


def parse_data(data):

    parsed_data = []
    for l in data:
        p = l.split('@')
        idx = int(p[0][1:])
        q = p[1].split(':')

        xy = tuple(int(x) for x in q[0].split(','))
        wh = tuple(int(x) for x in q[1].split('x'))

        parsed_data.append((idx, xy, wh))

    return parsed_data


with open("day3.txt") as f:
    data = f.readlines()

# data = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
parsed_data = parse_data(data)


def part1(data, size=1000):
    grid = np.zeros((size, size))
    for d in data:
        idx, xy, wh = d
        grid[xy[1]: xy[1] + wh[1], xy[0]: xy[0] + wh[0]] += 1

    print((grid >= 2).sum())


def part2(data, size=1000):
    grid = np.zeros((size, size))
    for d in data:
        idx, xy, wh = d
        grid[xy[1]: xy[1] + wh[1], xy[0]: xy[0] + wh[0]] += 1

    for d in data:
        idx, xy, wh = d
        if np.all(grid[xy[1]: xy[1] + wh[1], xy[0]: xy[0] + wh[0]] == 1):
            print(d)


part1(parsed_data)
part2(parsed_data)
