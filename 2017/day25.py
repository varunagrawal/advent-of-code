from tqdm import tqdm

def part1(steps):
    state = 'A'
    tape = [0 for _ in range(steps)]
    cursor = 0

    policy = {
        'A': {0: [1, 1, 'B'], 1: [1, -1, 'E']},
        'B': {0: [1, 1, 'C'], 1: [1, 1, 'F']},
        'C': {0: [1, -1, 'D'], 1: [0, 1, 'B']},
        'D': {0: [1, 1, 'E'], 1: [0, -1, 'C']},
        'E': {0: [1, -1, 'A'], 1: [0, 1, 'D']},
        'F': {0: [1, 1, 'A'], 1: [1, 1, 'C']},
    }

    for _ in tqdm(range(steps)):
        val, inc, state = policy[state][tape[cursor]]
        tape[cursor] = val
        cursor += inc

    print(sum(tape))

part1(12523873)