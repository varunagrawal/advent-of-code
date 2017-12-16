import numpy as np
import sys
sys.setrecursionlimit(15000) 


def knot_hash(s, lengths, start, skip):
    sz = len(s)
    for x in lengths:
        # ignore lengths greater than the list size
        if x > sz:
            continue

        # print("Original list", s)
        # print( start, x, skip)

        d = []
        for idx in range(x):
            d.append(s[(start+idx)%sz])
        
        # print(d)
        d = d[::-1]
        
        for idx in range(x):
            s[(start+idx)%sz] = d[idx]

        # print("new list", s)

        start = (start+x+skip) % sz
        skip += 1

    return s, start, skip

def preprocess_lengths(lengths):
    new_l = []
    for c in lengths:
        new_l.append(ord(c))

    new_l.extend([17, 31, 73, 47, 23])
    return new_l

def reduce(hash):
    dense_hash = []
    for i in range(0, len(hash), 16):
        val = 0
        for j in range(16):
            val = val^hash[i+j]
        dense_hash.append(val)
    return dense_hash

def hexadecimal(hash):
    s = ''
    for i in hash:
        h = hex(i)
        v = h.split('x')[-1]
        if len(v) == 1:
            v = '0'+v
        s += v
    return s

def compute_hash(lengths, input=256):
    s = [x for x in range(input)]
    lengths = preprocess_lengths(lengths)
    
    start, skip = 0, 0
    # run for 64 rounds
    for _ in range(64):
        s, start, skip = knot_hash(s, lengths, start, skip)
        # print(s)

    dense_hash = reduce(s)
    assert len(dense_hash) == 16

    hash_string = hexadecimal(dense_hash)
    return hash_string

def hash_to_bits(hash):
    bits = ""
    for x in hash:
        n = bin(int(x, 16))  # since this is a hex number
        bits += n.split('b')[-1].zfill(4)
    return bits

def part1(s):
    inp = "{0}-{1}"
    grid = np.zeros((128, 128))

    for i in range(128):
        x = inp.format(s, i)
        hash = compute_hash(x)
        bits = hash_to_bits(hash)

        assert len(bits) == 128
        # print(bits)
        for j, b in enumerate(bits):
            if b == '1':
                grid[i, j] = 1
            
    print(grid.sum())
    return grid

# part1("flqrgnkx")

def is_valid_coord(y, x, max=128):
    if x < 0 or y < 0 or x >= max or y >= max:
        return False
    return True

def flood_fill(i, j, val):
    if grid[i, j] == 0:
        return
    if region[i, j] > 0:
        return

    region[i, j] = val

    if i > 0:
        flood_fill(i-1, j, val)
    if j > 0:
        flood_fill(i, j-1, val)
    if i < 127:
        flood_fill(i+1, j, val)
    if j < 127:
        flood_fill(i, j+1, val)

def part2(grid):
    region_id = 0

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 0:
                continue
            if region[i, j] > 0:
                continue

            region_id += 1
            flood_fill(i, j, region_id)
            
    print(grid[:8, :8])
    print(region[:8, :8])
    print(region_id)

grid = part1("jzgqcdpd")
region = np.zeros(grid.shape)
part2(grid)
