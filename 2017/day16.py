import string
from tqdm import tqdm

def dance(programs, steps):
    for step in steps:
        if step[0] == 's':
            x = int(step[1:])
            for i in range(x):
                p = programs.pop()
                programs.insert(0, p)

        elif step[0] == 'x':
            x = step[1:]
            idx1, idx2 = [int(i) for i in x.split('/')]
            programs[idx1], programs[idx2] = programs[idx2], programs[idx1]
        
        elif step[0] == 'p':
            x = step[1:]
            p1, p2 = x.split('/')
            idx1 = programs.index(p1)
            idx2 = programs.index(p2)
            programs[idx1], programs[idx2] = programs[idx2], programs[idx1]
    return programs

def part1(steps):
    programs = list(string.ascii_lowercase[:16])
    programs = dance(programs, steps)
    print(''.join(programs))

def part2(steps):
    programs = list(string.ascii_lowercase[:16])
    seen = []
    reps = 1000000000
    for i in tqdm(range(reps)):
        s = ''.join(programs)
        if s in seen:
            print(seen[reps % i])
            return
        seen.append(s)
        programs = dance(programs, steps)
    print(''.join(programs))

with open('day16.in', 'r') as f:
    steps = f.read()

steps = steps.split(',')

part1(steps)

part2(steps)