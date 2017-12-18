from collections import defaultdict

def part1(instructions):
    registers = defaultdict(lambda: 0)
    last_sound_freq = -1

    pc = 0

    while pc < len(instructions):
        if "snd" in instructions[pc]:
            instr, r = instructions[pc].split(' ')
            last_sound_freq = registers[r]
        elif "set" in instructions[pc]:
            instr, r, v = instructions[pc].split(' ')
            if v.isalpha():
                v = registers[v]
            registers[r] = int(v)
        elif "add" in instructions[pc]:
            instr, r, v = instructions[pc].split(' ')
            if v.isalpha():
                v = registers[v]
            registers[r] += int(v)
        elif "mul" in instructions[pc]:
            instr, r, v = instructions[pc].split(' ')
            if v.isalpha():
                v = registers[v]
            registers[r] *= int(v)
        elif "mod" in instructions[pc]:
            instr, r, v = instructions[pc].split(' ')
            if v.isalpha():
                v = registers[v]
            registers[r] = registers[r] % int(v)
        elif "rcv" in instructions[pc]:
            instr, r = instructions[pc].split(' ')
            if registers[r] > 0:
                print("Recovered frequency is: ", last_sound_freq)
                exit(0)

        elif "jgz" in instructions[pc]:
            instr, r, v = instructions[pc].split(' ')
            if registers[r] > 0:
                pc = pc + int(v) - 1  # -1 because we increment pc later
        else:
            print("Invalid instruction. Exiting...")
            exit(0)
        
        pc += 1

with open("day18.in", 'r') as f:
    instructions = f.readlines()

for i in range(len(instructions)):
    instructions[i] = instructions[i].strip()

# part1(instructions)
    
class Program:
    def __init__(self, id, instructions):
        self.id = id
        self.instructions = instructions
        self.q = []
        self.pc = 0
        self.registers = defaultdict(lambda: 0)
        self.registers['p'] = id
        self.is_waiting = False
        self.send_counter = 0

    def set_other(self, program):
        self.other = program

    def print_result(self):
        if self.id == 0:
            print(self.other.send_counter)
        else:
            print(self.send_counter)
            
    def step(self):
        if self.pc < 0 or self.pc > len(self.instructions):
            self.print_result()
            exit(0)
    
        if "snd" in self.instructions[self.pc]:
            instr, r = self.instructions[self.pc].split(' ')
            self.other.q.append(self.registers[r])
            self.send_counter += 1
            # print(self.id, " sent value")

        elif "set" in self.instructions[self.pc]:
            instr, r, v = self.instructions[self.pc].split(' ')
            if v.isalpha():
                v = self.registers[v]
            self.registers[r] = int(v)
        
        elif "add" in self.instructions[self.pc]:
            instr, r, v = self.instructions[self.pc].split(' ')
            if v.isalpha():
                v = self.registers[v]
            self.registers[r] += int(v)
        
        elif "mul" in self.instructions[self.pc]:
            instr, r, v = self.instructions[self.pc].split(' ')
            if v.isalpha():
                v = self.registers[v]
            self.registers[r] *= int(v)
        
        elif "mod" in self.instructions[self.pc]:
            instr, r, v = self.instructions[self.pc].split(' ')
            if v.isalpha():
                v = self.registers[v]
            self.registers[r] = self.registers[r] % int(v)
        
        elif "rcv" in self.instructions[self.pc]:
            instr, r = self.instructions[self.pc].split(' ')
            if len(self.q) == 0:  # didn't receive anything
                self.is_waiting = True
                # print("Program {0} is waiting".format(self.id), len(self.other.q))

                if self.other.is_waiting:
                    print("Deadlock. Exiting...")
                    self.print_result()
                    exit(0)
                else:
                    self.pc -= 1
            else:                    
                self.is_waiting = False
                v = self.q.pop(0)
                self.registers[r] = v
                    
        elif "jgz" in self.instructions[self.pc]:
            instr, r, v = self.instructions[self.pc].split(' ')
            if v.isalpha():
                v = self.registers[v]
            
            # the register value in jgz can be a number instead of a register val
            if r.isalpha():
                x = self.registers[r]
            else:
                x = int(r)
            
            if x > 0:
                self.pc = self.pc + int(v) - 1  # -1 because we increment self.pc later
        
        else:
            print("Invalid instruction. Exiting...")
            exit(0)
        
        self.pc += 1

def part2(instructions):
    program0 = Program(0, instructions)
    program1 = Program(1, instructions)

    program0.set_other(program1)
    program1.set_other(program0)

    while True:
        program0.step()
        program1.step()

part2(instructions)