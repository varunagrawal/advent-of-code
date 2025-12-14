import numpy as np


def parse_data(data):
    db = []
    ingredients = []
    reading_ingredients = False
    for d in data:
        d = d.strip()
        if d == "":
            reading_ingredients = True
            continue

        if reading_ingredients:
            ingredients.append(int(d))
        else:
            db.append([int(x) for x in d.strip().split("-")])

    return db, ingredients


def part1(data):
    db, ingredients = parse_data(data)

    fresh_count = 0
    for ingredient in ingredients:
        for lower, upper in db:
            if lower <= ingredient <= upper:
                fresh_count += 1
                break

    print(fresh_count)


def part2(data):
    db, _ = parse_data(data)

    intervals = sorted(db, key=lambda x: x[0])
    merged_intervals = []
    last_merged = intervals[0]

    for interval in intervals[1:]:
        if last_merged[1] >= interval[0]:
            last_merged = [last_merged[0], max(last_merged[1], interval[1])]
        else:
            merged_intervals.append(last_merged)
            last_merged = interval

    merged_intervals.append(last_merged)

    result = 0
    for interval in merged_intervals:
        result += interval[1] - interval[0] + 1

    # print(merged_intervals)
    print(result)


def test():
    data = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]

    part1(data)
    part2(data)


def main():
    with open("day5.in") as f:
        data = f.readlines()

    part1(data)
    part2(data)


if __name__ == "__main__":
    # test()
    main()
