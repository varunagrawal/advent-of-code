def part1(instructions):
    registers = {}
    for c in 'abcdefgh':
        registers[c] = 0

    count = 0

    pc = 0

    while pc >= 0 and pc < len(instructions):
        # print(pc, instructions[pc])

        cmd, x, y = instructions[pc].split()

        if cmd == 'set':
            if y.isalpha():
                registers[x] = registers[y]
            else:
                registers[x] = int(y)
            
        elif cmd == 'sub':
            if y.isalpha():
                registers[x] -= registers[y]
            else:
                registers[x] -= int(y)
            
        elif cmd == 'mul':
            if y.isalpha():
                registers[x] *= registers[y]
            else:
                registers[x] *= int(y)
            count += 1
            
        elif cmd == 'jnz':
            if x.isalpha():
                x = registers[x]
            else:
                x = int(x)
            if y.isalpha():
                y = registers[y]
            else:
                y = int(y)
            
            if x != 0:
                pc = pc + y - 1
            
        # print(pc)
        # print(registers)
        # if registers['g'] == 0 or pc > 20:
        #     input()
        pc += 1

    print(count)
    print(registers)

def part2():
    """
    What the assembly does is basically check how many composite numbers exist between the two ends
    """
    # got these numbers from decompiling the assembly input
    start = 108100
    end = 125100
    inc = 17
    h = 0

    for x in range(start, end+1, inc):
        # do a sieve of Eratosthenes
        for i in range(2, x):
            if x % i == 0:
                h += 1
                break
        
    print(h)

with open("day23.in", 'r') as f:
    instrs = f.readlines()

part1(instrs)

part2()               
