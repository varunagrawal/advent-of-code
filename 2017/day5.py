import argparse


def perform_jump(arr, idx):
    offset = arr[idx]
    if offset >= 3:
        delta = -1
    else:
        delta = 1
    arr[idx] += delta
    idx += offset

    return idx, arr


def main(inp):
    with open(inp, 'r') as f:
        arr = f.read()

    arr = arr.split('\n')
    arr = [int(x.strip()) for x in arr]

    curr_index = 0
    n_steps = 0
    # print(arr)
    
    # print(arr)
    while curr_index < len(arr):
        curr_index, arr = perform_jump(arr, curr_index)
        n_steps += 1

    return n_steps


print(main("day5.in"))
