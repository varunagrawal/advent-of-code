from collections import Counter
from math import ceil


def get_range(r):
    lower, upper = r.split("-")
    return (int(lower), int(upper))


def is_invalid_id_1(number: str) -> bool:
    """
    The idea here is that an ID is invalid if it is entirely made up of a sequence repeated twice.
    So the simplest idea is to split the string in half, and check if each half matche.
    """
    if len(number) % 2 == 1:  # odd length numbers are automatically disqualified
        return False

    mid = len(number) // 2
    return number[0:mid] == number[mid:]


def part1(inputs):
    ranges = [get_range(r) for r in inputs.split(",")]

    sum_invalid_ids = 0

    for lower, upper in ranges:
        for i in range(lower, upper + 1):  # include upper
            if is_invalid_id_1(str(i)):
                sum_invalid_ids += i

    print(sum_invalid_ids)


def is_invalid_id_2(number: str) -> bool:
    for m in range(1, len(number)):
        substrs = [number[i * m : (i + 1) * m] for i in range(ceil(len(number) / m))]

        counter = Counter(substrs)

        if len(counter) == 1 and counter[list(counter.keys())[0]] >= 2:
            return True

    return False


def part2(inputs):
    ranges = [get_range(r) for r in inputs.split(",")]

    sum_invalid_ids = 0

    for lower, upper in ranges:
        for i in range(lower, upper + 1):  # include upper
            if is_invalid_id_2(str(i)):
                sum_invalid_ids += i

    print(sum_invalid_ids)


def test():
    inputs = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    # inputs = "11-22,95-115,998-1012"
    part1(inputs)
    part2(inputs)


def main():
    with open("day2.in") as f:
        inputs = f.readlines()[0]

    # part1(inputs)
    part2(inputs)


if __name__ == "__main__":
    # test()
    main()
