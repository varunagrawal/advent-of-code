import string


def collapse(polymer):
    i = 0
    reaction = False

    while True:
        if i >= len(polymer) - 1:
            if reaction == False:
                break
            i = 0
            reaction = False

        if polymer[i].isupper() and polymer[i].lower() == polymer[i+1]:
            # print(i, i+1, polymer[i], polymer[i+1])
            polymer = polymer[:i] + polymer[i+1+1:]
            reaction = True

        elif polymer[i].islower() and polymer[i].upper() == polymer[i+1]:
            # print(i, i+1, polymer[i], polymer[i+1])
            polymer = polymer[:i] + polymer[i+1+1:]
            reaction = True

        else:
            i += 1
    return polymer


def part1(polymer):
    polymer = collapse(polymer)

    # print(polymer)
    print(len(polymer))


def part2(polymer):
    min_len = len(polymer)
    for c in string.ascii_lowercase:
        print(c)
        polymer_sub = polymer.replace(c, '').replace(c.upper(), '')
        collapsed_polymer = collapse(polymer_sub)

        if len(collapsed_polymer) < min_len:
            min_len = len(collapsed_polymer)

    print(min_len)


s = "dabAcCaCBAcCcaDA"
with open("day5.txt") as f:
    s = f.read()

# print(len(s))

part1(s)

part2(s)
