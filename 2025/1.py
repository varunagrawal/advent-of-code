MAX = 100


def modulo_minus(dial, distance, part2: bool = False):
    num_zeros = 0

    def minus(dial, distance, zeros):
        was_positive = dial > 0

        dial -= distance

        if dial == 0:
            zeros += 1

        if dial < 0:
            dial += MAX
            if was_positive and part2:
                zeros += 1

        return dial, zeros

    if abs(distance) > MAX and part2:
        num_zeros += distance // MAX

    dial, num_zeros = minus(dial, distance % MAX, num_zeros)
    return dial, num_zeros


def modulo_plus(dial, distance, part2: bool = False):
    num_zeros = 0

    def plus(dial, distance, zeros):
        dial += distance

        if dial == MAX:
            dial = 0
            zeros += 1

        if dial > MAX:
            dial -= MAX
            if part2:
                zeros += 1

        return dial, zeros

    if abs(distance) > MAX and part2:
        num_zeros += distance // MAX

    dial, num_zeros = plus(dial, distance % MAX, num_zeros)
    return dial, num_zeros


def test():
    inputs = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    dial = 50
    num_zeros = 0

    for line in inputs:
        distance = int(line[1:])

        if line[0] == "L":
            t = modulo_minus(dial, distance, True)
            dial = t[0]
            num_zeros += t[1]

        elif line[0] == "R":
            t = modulo_plus(dial, distance, True)
            dial = t[0]
            num_zeros += t[1]

        print(f"After {line}, dial is at {dial} and {num_zeros=}")

    print(num_zeros)


def part1(lines: list[str]):
    dial = 50
    num_zeros = 0

    for line in lines:
        distance = int(line[1:])

        if line[0] == "L":
            t = modulo_minus(dial, distance)
            dial = t[0]
            num_zeros += t[1]

        elif line[0] == "R":
            t = modulo_plus(dial, distance)
            dial = t[0]
            num_zeros += t[1]

        # print(f"After {line[0]}{int(line[1:])}, dial is {dial}")

    print(num_zeros)


def part2(lines: list[str]):
    dial = 50
    num_zeros = 0

    for line in lines:
        distance = int(line[1:])

        if line[0] == "L":
            t = modulo_minus(dial, distance, part2=True)
            dial = t[0]
            num_zeros += t[1]

        elif line[0] == "R":
            t = modulo_plus(dial, distance, part2=True)
            dial = t[0]
            num_zeros += t[1]

        # print(f"After {line[0]}{int(line[1:])}, dial is {dial}")

    print(num_zeros)

def main():
    with open("day1.in") as f:
        lines = f.readlines()

    part1(lines)
    part2(lines)


if __name__ == "__main__":
    # test()
    main()
