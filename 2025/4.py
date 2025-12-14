import numpy as np


def create_map(inp):
    # Add padding around the map
    num_rows = len(inp) + 2
    num_cols = len(inp[0]) + 2

    # Create map
    full_map = np.zeros((num_rows, num_cols))

    for r in range(1, num_rows - 1):
        for c in range(1, num_cols - 1):
            if inp[r - 1][c - 1] == "@":
                full_map[r, c] = 1

    return full_map


def check_neighbors(full_map, r, c):
    """Return true if <= 4 paper rolls in the neighbors of (r, c)."""
    neighbors = 0
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i == 0 and j == 0:
                continue

            # if r == 1 and c == 6:
            #     print(">>", i, j, full_map[r + i, c + j])
            neighbors += full_map[r + i, c + j]

    return neighbors < 4


def test():
    inp = [
        "..@@.@@@@.",
        "@@@.@.@.@@",
        "@@@@@.@.@@",
        "@.@@@@..@.",
        "@@.@@@@.@@",
        ".@@@@@@@.@",
        ".@.@.@.@@@",
        "@.@@@.@@@@",
        ".@@@@@@@@.",
        "@.@.@@@.@.",
    ]

    full_map = create_map(inp)
    num_rows, num_cols = full_map.shape
    print(full_map[1:-1, 1:-1])

    result = 0
    for r in range(1, num_rows - 1):
        for c in range(1, num_cols - 1):
            if full_map[r, c] > 0 and check_neighbors(full_map, r, c):
                result += 1

    print(result)


def part1(inp):
    full_map = create_map(inp)
    num_rows, num_cols = full_map.shape

    result = 0
    for r in range(1, num_rows - 1):
        for c in range(1, num_cols - 1):
            if full_map[r, c] > 0 and check_neighbors(full_map, r, c):
                result += 1

    print(result)


def part2(inp):
    full_map = create_map(inp)
    num_rows, num_cols = full_map.shape

    result = 0

    while True:
        removal_map = np.array(full_map)
        removed = 0

        for r in range(1, num_rows - 1):
            for c in range(1, num_cols - 1):
                if full_map[r, c] > 0 and check_neighbors(full_map, r, c):
                    removal_map[r, c] = 0
                    removed += 1

        if removed == 0:
            break

        result += removed
        full_map = full_map * removal_map

    print(result)


def main():
    with open("day4.in") as f:
        inp = f.readlines()
        inp = [l.strip() for l in inp]

    part1(inp)
    part2(inp)


if __name__ == "__main__":
    # test()
    main()
