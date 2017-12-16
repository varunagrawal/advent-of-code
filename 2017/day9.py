def part1(s):
    stack = []
    garbage = False
    sum = 0

    i = 0
    while i < len(s):
        if s[i] == '{':
            if not garbage:
                stack.append('{')
        elif s[i] == '}':
            if not garbage:
                sum += len(stack)
                stack.pop()
        elif s[i] == '!':
            i += 1
        elif s[i] == '<':
            garbage = True
        elif s[i] == '>':
            garbage = False

        i += 1

    return sum

inputs = [("{}", 1), ("{{{}}}", 6), ("{{},{}}", 5), ("{{{},{},{{}}}}", 16), ("{{<!!>},{<!!>},{<!!>},{<!!>}}", 9), ("{{<a!>},{<a!>},{<a!>},{<ab>}}", 3)]

# for inp, val in inputs:
    # print(part1(inp), val)

with open("day9.in", 'r') as f:
    s = f.read()
# print("Part 1 ans: ", part1(s))

def part2(s):
    sum = 0
    i = 0
    start = False
    cnt = 0
    
    while i < len(s):
        if s[i] == '<':
            if not start:
                cnt = 0
                start = True
            else:
                cnt += 1
        elif s[i] == '!':
            i += 1
        elif s[i] == '>':
            start = False
            sum += cnt
        else:
            cnt += 1
        
        i += 1
    
    return sum

print(part2(s))