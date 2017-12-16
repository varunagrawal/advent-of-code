"""
We need Hexagonal coordinate systems to solve this: https://www.redblobgames.com/grids/hexagons/
"""

def hexagon_dist(x, y, z):
    dist = (abs(x) + abs(y) + abs(z)) / 2
    return dist

def hex_ed(seq):
    x, y, z = 0, 0, 0
    distances = []

    for d in seq:
        if d == 'n':
            x += 1
            z -= 1
        elif d == 'ne':
            x += 1
            y -= 1
        elif d == 'se':
            z += 1
            y -= 1
        elif d == 's':
            z += 1
            x -= 1
        elif d == 'sw':
            x -= 1
            y += 1
        elif d == 'nw':
            z -= 1
            y += 1

        distances.append(hexagon_dist(x, y, z))
    
    print(max(distances))
    dist = hexagon_dist(x, y, z)
    return dist

with open("day11.in", 'r') as f:
    x = f.read()

print(hex_ed(x.split(',')))
