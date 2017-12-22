import numpy as np

def parse(d):
    d = d.split('/')
    o = np.zeros((len(d), len(d[0])), dtype=np.str)
    for i, k in enumerate(d):
        for j, l in enumerate(k):
            o[i, j] = l
        
    return o

def parse_rules(lines):
    rules = []
    for l in lines:
        inp, out = l.split(' => ')
        rules.append((parse(inp), parse(out)))

    return rules

flips = [lambda x:x, np.fliplr, np.flipud]
rotations = [lambda x: np.rot90(x, k=0), lambda x: np.rot90(x, k=3), lambda x: np.rot90(x, k=2), lambda x: np.rot90(x, k=1)]

def process(x, rule):
    for r in rotations:
        x = r(x)

        for f in flips:
            e = f(x)

            if np.array_equal(e, rule[0]):
                return rule[1]
    return None


def two(arr, rules):
    """The input is divisible by 2"""
    rows, cols = arr.shape
    x = np.zeros(((rows//2)*3, (cols//2)*3), dtype=np.str)    

    for i in range(rows//2):
        for j in range(cols//2):
            d = arr[2*i:2*i+2, 2*j:2*j+2]
            # print(d)
            for rule in rules:
                val = process(d, rule)
                if val is not None:
                    x[3*i:3*i+3, 3*j:3*j+3] = val
                    break
    return x

def three(arr, rules):
    """The input is divisible by 3"""
    rows, cols = arr.shape
    x = np.zeros(((rows//3)*4, (cols//3)*4), dtype=np.str)

    for i in range(rows//2):
        for j in range(cols//2):
            d = arr[3*i:3*i+3, 3*j:3*j+3]
            # print(d)
            for rule in rules:
                val = process(d, rule)
                if val is not None:
                    x[4*i:4*i+4, 4*j:4*j+4] = val
                    break
    return x

def part1(data):
    rules = parse_rules(data)
    x = np.array([['.', '#', '.'], ['.', '.', '#'], ['#', '#', '#']], dtype=np.str)
    # print(three(x, rules))
    # x = np.array([['#', '.', '.', '#'], ['.', '.', '.', '.'], ['.', '.', '.', '.'], ['#', '.', '.', '#']], dtype=np.str)
    # print(two(x, rules))
    
    for i in range(18):
        if x.shape[0] % 2 == 0:
            x = two(x, rules)
        elif x.shape[0] % 3 == 0:
            x = three(x, rules)

        # print(x)
        print(i)
        
    count = 0
    for row in x:
        for c in row:
            if c == '#':
                count += 1

    print(count)

# print(parse_rules(["../.# => ##./#../..."]))
with open('day21.in', 'r') as f:
    data = f.readlines()

data = [d.strip() for d in data]
part1(data)