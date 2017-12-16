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


def part1(lengths, input=256):
    s = [x for x in range(input)]
    start, skip = 0, 0

    s, _, _ = knot_hash(s, lengths, start, skip)
        # print(s)

    return s[0] * s[1]

# print(part1([3, 4, 1, 5], input=5))
# print(part1([197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63]))


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

def part2(lengths, input=256):
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

# print(part2([3, 4, 1, 5], input=5))

# assert reduce([65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22]) == [64]
# assert hexadecimal([64, 7 ,255]) == '4007ff'
# print(part2('1,2,3'))
assert part2('AoC 2017') == "33efeb34ea91902bb2f59c9920caa6cd"
print(part2('197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63'))

