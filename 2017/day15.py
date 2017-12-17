from tqdm import tqdm

def generate(val, factor):
    x = val * factor
    x = x % 2147483647
    return x

a_val = 65#783
b_val = 8921#325

a_vals, b_vals = [], []

def part1(a_val, b_val):
    count = 0

    for i in tqdm(range(40000000)):  # 40000000
        a_val = generate(a_val, 16807)
        b_val = generate(b_val, 48271)

        # print(a_val, "\t", b_val)

        a_bin = bin(a_val).split('b')[-1].zfill(32)
        b_bin = bin(b_val).split('b')[-1].zfill(32)

        if a_bin[-16:] == b_bin[-16:]:
            count += 1
    print(count)

# part1(65, 8921)

def part2(a_val, b_val):
    while True:  # 5000000
        a_val = generate(a_val, 16807)
        b_val = generate(b_val, 48271)

        if a_val % 4 == 0:
            a_vals.append(a_val)
        if b_val % 8 == 0:
            b_vals.append(b_val)

        if len(a_vals) >= 5000000 and len(b_vals) >= 5000000:
            break

    n = min(len(a_vals), len(b_vals))
    count = 0

    for i in range(n):
        a_bin = bin(a_vals[i]).split('b')[-1].zfill(32)
        b_bin = bin(b_vals[i]).split('b')[-1].zfill(32)

        if a_bin[-16:] == b_bin[-16:]:
            count += 1

    print(count)

part2(783, 325)
part2(65, 8921)
