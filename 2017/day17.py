from tqdm import tqdm

def spinlock(buffer, cur_pos, steps, num):
    for i in tqdm(range(num)):
        cur_pos = (cur_pos + steps) % len(buffer)
        cur_pos += 1
        buffer.insert(cur_pos, i+1)
    return buffer, cur_pos


def part1(steps):
    buffer = [0]
    cur_pos = 0

    buffer, cur_pos = spinlock(buffer, cur_pos, steps, 2017)
    print(buffer[(cur_pos + 1) % len(buffer)])

def part2(steps):
    buffer = [0]
    cur_pos = 0

    # buffer = spinlock(buffer, cur_pos, steps, 50000000)
    # pos = buffer.index(0)
    # print(buffer[(pos+1) % len(buffer)])

    # using a list for the buffer is too slow as we add numbers
    # trick is that we only look for insertions after 0 so we don't really care about previous insertions
    sz = 1
    for i in tqdm(range(50000000)):
        cur_pos = (cur_pos + steps) % sz
        cur_pos += 1
        x = i + 1
        if cur_pos == 1:
            val = x
        sz += 1
    print(val)

# part1(3)
# part1(303)

part2(303)
