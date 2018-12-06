import numpy as np
from collections import defaultdict


def manhattan_dist(x, y):
    return np.abs(x[0] - y[0]) + np.abs(x[1] - y[1])


def part1(data):
    xs = [x[0] for x in data]
    ys = [x[1] for x in data]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    grid = -np.ones((max_y+1, max_x+1))

    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            min_dist = np.inf
            idx = -1
            # this variable keeps track of how many points are min dist away from (x, y)
            closest_count = 0
            for i, coord in enumerate(data):
                dist = manhattan_dist(coord, (x, y))
                if dist < min_dist:
                    idx = i
                    min_dist = dist
                    closest_count = 1
                elif dist == min_dist and idx > -1:
                    closest_count += 1

            if closest_count > 1:
                idx = -1

            grid[y, x] = idx

    # print(grid)

    areas = []
    for i, x in enumerate(data):
        if (x[0] == min_x or x[1] == min_y) or (x[0] == max_x or x[1] == max_y):
            # check if the point lies on the extrema of the grid
            # if yes, skip
            continue
        elif i in grid[0, :] or i in grid[-1, :] \
                or i in grid[:, 0] or i in grid[:, -1]:
                # this checks if the index of the data point lies on the grid boundary
                # this would indicate that the area extends to infinity, so we skip
            continue
        # print(i, data[i], (grid == i).sum())
        areas.append((grid == i).sum())

    print(max(areas))


def part2(data, threshold=10000):
    xs = [x[0] for x in data]
    ys = [x[1] for x in data]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    # this grid records the sum of distances to each coord for every point on the grid
    grid = np.zeros((max_y+1, max_x+1))

    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            sum_dist = 0
            for i, coord in enumerate(data):
                sum_dist += manhattan_dist(coord, (x, y))

            # print(sum_dist)
            grid[y, x] = sum_dist

    # print(grid < threshold)
    print((grid < threshold).sum())


data = [(1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9)]

with open("day6.txt") as f:
    d = f.readlines()
    data = []
    for l in d:
        x = l.strip().split(',')
        data.append((int(x[0]), int(x[1])))

part1(data)
part2(data)
