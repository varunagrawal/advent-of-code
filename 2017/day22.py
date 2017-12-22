import numpy as np
from tqdm import tqdm

def parse_input(data):
    map = np.zeros((len(data), len(data[0])))
    for i, row in enumerate(data):
        for j, c in enumerate(row):
            if c == '#':
                map[i, j] = 1
    return map

class Virus:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir = 0  # 0 is up

    def step(self):
        if self.dir == 0:  # up
            self.y -= 1
        elif self.dir == 1:  # right
            self.x += 1
        elif self.dir == 2:  # down
            self.y += 1
        elif self.dir == 3:  # left
            self.x -= 1


def part1(map):
    # virus = Virus(map.shape[0]//2, map.shape[1]//2)
    virus = Virus(500, 500)

    infected = 0

    for i in range(10000):
        # print(virus.y, virus.x)
        if map[virus.y, virus.x] == 1:  # infected
            virus.dir = (virus.dir + 1) % 4
            map[virus.y, virus.x] = 0

        elif map[virus.y, virus.x] == 0:  # not infected
            virus.dir = (virus.dir - 1) % 4
            map[virus.y, virus.x] = 1
            infected += 1

        virus.step()
        # print(virus.dir)
    # print(map)
    print(infected)

def part2(map):
    # virus = Virus(500, 500)
    virus = Virus(map.shape[0]//2, map.shape[1]//2)

    states = [0, 1, 2, 3]  # clean, weakened, infected, flagged ->
    infected = 0

    for i in tqdm(range(10000000)):
        # print(virus.y, virus.x)
        if map[virus.y, virus.x] == 0:  # not infected
            virus.dir = (virus.dir - 1) % 4
            map[virus.y, virus.x] = (map[virus.y, virus.x] + 1) % 4

        elif map[virus.y, virus.x] == 1:  # weakened
            # does not turn
            # infect the node
            map[virus.y, virus.x] = (map[virus.y, virus.x] + 1) % 4
            infected += 1
            
        elif map[virus.y, virus.x] == 2:  # infected
            virus.dir = (virus.dir + 1) % 4
            map[virus.y, virus.x] = (map[virus.y, virus.x] + 1) % 4
            
        elif map[virus.y, virus.x] == 3:  # flagged
            virus.dir = (virus.dir + 2) % 4  # reverse direction
            map[virus.y, virus.x] = (map[virus.y, virus.x] + 1) % 4

        virus.step()

        # print(virus.dir)
    # print(map)
    print(infected)

with open("day22.in", 'r') as f:
    data = f.read().split('\n')

c_map = parse_input(data)
# print(map.shape)
map = np.zeros((1000, 1000))
map[500-c_map.shape[0]//2:500+c_map.shape[0]//2 + 1, 500-c_map.shape[1]//2:500+c_map.shape[1]//2 + 1] = c_map

part1(map)

# reinitialize map since part 1 updates the original map
map = np.zeros((1000, 1000))
map[500-c_map.shape[0]//2:500+c_map.shape[0]//2 + 1, 500-c_map.shape[1]//2:500+c_map.shape[1]//2 + 1] = c_map
map = map*2
part2(map)
