import argparse
from collections import defaultdict


def parse_input():
    with open("day8.in", 'r') as f:
        d = f.readlines()

    return d


def part1():
    instrs = parse_input()
    # initialize registers to 0
    registers = defaultdict(lambda: 0) 

    overall_max = 0

    for instr in instrs:
        l = instr.split()
        register, op, val, _, a, cond, b = l

        # print(' '.join([str(registers[a]), cond, b]))
        result = eval(' '.join([str(registers[a]), cond, b]))
        # print(result)

        if result:
            if op == 'inc':
                registers[register] += int(val)
            elif op == 'dec':
                registers[register] -= int(val)

        new_max = max(list(registers.values()))
        if new_max > overall_max:
            overall_max = new_max
        # print(registers)
        # print()

    max_val = max(list(registers.values()))
    print(max_val)

    print("Highest max at any time:", overall_max)
    

part1()
