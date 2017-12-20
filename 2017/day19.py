import numpy as np
import string

def is_valid(i, j, rows, cols):
    return i >= 0 and j >= 0 and i < rows and j < cols

def part1(map):
    i, j = 0, 0
    # find the starting point
    for k, d in enumerate(map[i]):
        if d == '|':
            j = k

    rows, cols = len(map), len(map[0])
    visited = np.zeros((rows, cols))

    letters = ""
    x, y = 0, 1
    steps = 0

    while True:
        # print(i, j)
        visited[i, j] = steps+1
        
        # print(map[i][j])

        if map[i][j] == '|':
            i += y
            j += x
            # print("Incremented I to ", i)
        elif map[i][j] == '-':
            i += y
            j += x
            # print("Incremented J to ", j)
        elif map[i][j] == '+':
            if is_valid(i+1, j, rows, cols) and map[i+1][j] != ' ' and visited[i+1, j] == 0:
                y = 1
                x = 0
                i += y
                # print("Incremented I")
            elif is_valid(i-1, j, rows, cols) and map[i-1][j] != ' ' and visited[i-1, j] == 0:
                y = -1
                x = 0
                i += y
                # print("Decremented I")
            elif is_valid(i, j+1, rows, cols) and map[i][j+1] != ' ' and visited[i, j+1] == 0:
                x = 1
                y = 0
                j += x
                # print("Incremented J to ", j)
            elif is_valid(i, j-1, rows, cols) and map[i][j-1] != ' ' and visited[i, j-1] == 0:
                x = -1
                y = 0
                j += x
                # print("Decremented J")
            else:
                break
        elif map[i][j] in string.ascii_letters:
            letters += map[i][j]
            i += y
            j += x
            # print("Found alphabet")
        else:
            # print("Breaking out")
            break

        steps += 1

    print(visited)
    print(letters)
    print(steps)

with open("day19.in", 'r') as f:
    map = f.readlines()

part1(map)