def compute_joltage(bank, num_batteries):
    joltage = ""
    start_index = 0

    for n in range(num_batteries, 0, -1):
        max_charge = int(bank[start_index])
        for i in range(start_index, len(bank) - n + 1):
            charge = int(bank[i])
            if charge > max_charge:
                start_index = i
                max_charge = charge

        joltage += bank[start_index]

        # increment start_index for the next iteration
        start_index += 1

    return int(joltage)


def part1(banks):
    joltage_sum = 0
    for bank in banks:
        ## Naive way, superseded by compute_joltage
        # first_index = 0
        # for i in range(len(bank) - 1):
        #     v = bank[i]
        #     if int(v) > int(bank[first_index]):
        #         first_index = i

        # second_index = first_index + 1
        # for j in range(first_index + 1, len(bank)):
        #     v = bank[j]
        #     if int(v) > int(bank[second_index]):
        #         second_index = j

        # joltage = int(f"{bank[first_index]}{bank[second_index]}")
        joltage = compute_joltage(bank, 2)
        # print(joltage)

        joltage_sum += joltage

    print(f"Total joltage is {joltage_sum}")


def part2(banks):
    joltage_sum = 0
    for bank in banks:
        joltage = compute_joltage(bank, 12)

        joltage_sum += joltage

    print(f"Total joltage is {joltage_sum}")


def test():
    banks = [
        "987654321111111",
        "811111111111119",
        "234234234234278",
        "818181911112111",
    ]
    part1(banks)
    part2(banks)


def main():
    with open("day3.in") as f:
        banks = f.readlines()
    banks = [bank.strip() for bank in banks]

    part1(banks)
    part2(banks)


if __name__ == "__main__":
    # test()
    main()
