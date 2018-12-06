import numpy as np


def parse_line(line):
    datetime, txt = line.strip().split(']')
    datetime = datetime[1:]
    date, time = datetime.split()
    hh, mm = time.split(':')
    return date, hh, mm, txt.strip()


def get_guard_id(txt):
    return txt.split("begins")[0][7:].strip()


def part1(data):
    number_of_guards = 0
    guard_idx = {}
    d = []
    for line in data:
        date, hh, mm, txt = parse_line(line)
        d.append((" ".join([date, hh, mm]), (hh, mm), txt))
        if "Guard" in txt:
            gid = get_guard_id(txt)
            if gid in guard_idx.keys():
                continue
            guard_idx[gid] = number_of_guards
            number_of_guards += 1

    d = sorted(d, key=lambda x: x[0])
    sleep_times = np.zeros((number_of_guards, 60))

    for x in d:
        timestamp, (hh, mm), txt = x
        if "Guard" in txt:
            gid = get_guard_id(txt)
        elif "falls asleep" in txt:
            start = int(mm)
        elif "wakes up" in txt:
            end = int(mm)
            sleep_times[guard_idx[gid], start:end] += 1

    # print(guard_idx)
    # print(sleep_times)
    max_idx = sleep_times.sum(axis=1).argmax()
    max_gid = next(x for x in guard_idx.keys() if guard_idx[x] == max_idx)
    max_min = sleep_times[max_idx, :].argmax()
    print(max_idx, max_gid, max_min, int(max_gid) * max_min)


def part2(data):
    number_of_guards = 0
    guard_idx = {}
    d = []
    for line in data:
        date, hh, mm, txt = parse_line(line)
        d.append((" ".join([date, hh, mm]), (hh, mm), txt))
        if "Guard" in txt:
            gid = get_guard_id(txt)
            if gid in guard_idx.keys():
                continue
            guard_idx[gid] = number_of_guards
            number_of_guards += 1

    d = sorted(d, key=lambda x: x[0])
    sleep_times = np.zeros((number_of_guards, 60))

    for x in d:
        timestamp, (hh, mm), txt = x
        if "Guard" in txt:
            gid = get_guard_id(txt)
        elif "falls asleep" in txt:
            start = int(mm)
        elif "wakes up" in txt:
            end = int(mm)
            sleep_times[guard_idx[gid], start:end] += 1

    max_idx = np.unravel_index(sleep_times.argmax(), sleep_times.shape)
    max_gid = next(x for x in guard_idx.keys() if guard_idx[x] == max_idx[0])
    print(int(max_gid) * max_idx[1])


data = ["[1518-11-01 00:00] Guard #10 begins shift",
        "[1518-11-01 00:05] falls asleep",
        "[1518-11-01 00:25] wakes up",
        "[1518-11-01 00:30] falls asleep",
        "[1518-11-01 00:55] wakes up",
        "[1518-11-01 23:58] Guard #99 begins shift",
        "[1518-11-02 00:40] falls asleep",
        "[1518-11-02 00:50] wakes up",
        "[1518-11-03 00:05] Guard #10 begins shift",
        "[1518-11-03 00:24] falls asleep",
        "[1518-11-03 00:29] wakes up",
        "[1518-11-04 00:02] Guard #99 begins shift",
        "[1518-11-04 00:36] falls asleep",
        "[1518-11-04 00:46] wakes up",
        "[1518-11-05 00:03] Guard #99 begins shift",
        "[1518-11-05 00:45] falls asleep",
        "[1518-11-05 00:55] wakes up"]
        
with open("day4.txt") as f:
    data = f.readlines()

part1(data)
part2(data)
