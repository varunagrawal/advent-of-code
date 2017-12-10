"""Solution for day 3"""

import numpy as np


def steps(x):
    i = 1
    while True:
        if x < i*i:
            break
        i += 2
    top_left = (i-1)*(i-1) + 1
    bottom_right = (i-2)*(i-2)
    top_right = bottom_right + (top_left - bottom_right) // 2
    bottom_left = top_left + (i*i - top_left) // 2

    print(bottom_right)
    if x == bottom_right:
        return i-2-1

    elif x == top_left:
        return i-1

    elif x == bottom_left or x == top_right:
        # same distance as top left corner due to symmetry
        return i-1

    elif x < top_right:
        if top_right - x < x - bottom_right:
            return i-1 - (top_right - x)
        elif top_right - x > x - bottom_right:
            return (i-1) - (x - bottom_right)
        else:
            return (i-1)//2

    elif x < top_left and x > top_right:
        if top_left - x < x - top_right:  # closer to top left
            return i - 1 - (top_left - x)
        elif top_left - x > x - top_right:
            return i - 1 - (x - top_right)
        else:
            return (i-1)//2
    elif x < bottom_left and x > top_left:
        if bottom_left - x < x - top_left:
            return i - 1 - (bottom_left - x)
        elif bottom_left - x > x - top_left:
            return i - 1 - (x - top_left)
        else:
            return (i-1)//2
    elif x > bottom_left:
        next = i*i
        if next - x < x - bottom_left:
            return i - 1 - (next-x)
        elif next - x > x - bottom_left:
            return i - 1 - (x - bottom_left)
        else:
            return (i-1)//2
    
def part1():
    tests = [(5, 2), (9, 2), (13, 4), (15, 2), (17, 4), (23, 2), (25, 4), (49, 6)]
    for t in tests:
        print(t[0], steps(t[0]), t[1])

    print(steps(312051))


class SpiralWalker:
    def __init__(self):
        self.direction = 'r'
        self.directions = ['r', 'u', 'l', 'd']
        self.spiral = np.zeros((558, 558)) * -1
        self.position = [0, 0]

    def toggle_direction(self):
        idx = self.directions.index(self.direction)
        self.direction = self.directions[(idx+1) % len(self.directions)]

    def step(self):
        if self.direction == 'r':
            self.position[1] += 1

        elif self.direction == 'l':
            self.position[1] -= 1
        elif self.direction == 'u':
            self.position[0] += 1
        elif self.direction == 'd':
            self.position[0] -= 1
        
    def print(self):
        print(self.spiral)


def get_value(spiral, x, y):
    val = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            val += spiral[y+j, x+i]
    return val


def part2(inp):
    l = int(np.sqrt(inp)) + 2
    spiral = np.zeros((l, l))
    x, y = l // 2, l // 2
    spiral[y, x] = 1

    directions = ['>', '^', '<', 'v']

    direction = directions[0]
    idx = 0
    turns = 0
    steps = 1
    counter = 1
    limit = 1

    while True:
        if direction == '>':
            x += 1
        elif direction == '<':
            x -= 1
        elif direction == '^':
            y -= 1
        elif direction == 'v':
            y += 1
        
        if x >= l or y >= l:
            break

        # take a step
        steps += 1
        counter += 1
        val = get_value(spiral, x, y)
        spiral[y, x] = val
        
        if val > inp:
            print(val)
            return

        # turn since we've reached the limit for the current direction
        if steps >= limit:
            idx = (idx + 1) % len(directions)
            direction = directions[idx]
            if direction in ['>', '<']: # move in left or right direction
                limit += 1 
            steps = 0

    # print(spiral)

# part2(9)
part2(312051)
