import argparse
import numpy as np


# List of strings representing the various states
# used for comparison
states = []
loops = []

def get_state(banks):
    return " ".join(str(x) for x in banks)

def reallocate(banks, idx):
    val = banks[idx]
    banks[idx] = 0
    for i in range(val):
        banks[(idx+i+1)%len(banks)] += 1
    return banks

def main(banks):
    states.append(get_state(banks))
    n_redist = 0
    curr_loop = 0
    loops.append(curr_loop)
    
    # print(states)
    while True:
        curr_loop += 1
        n_redist += 1
        # argmax automatically returns the 1st index with max value
        max_bank = np.argmax(banks)  

        banks = reallocate(banks, max_bank)
        
        state = get_state(banks)
        if state in states:
            idx = states.index(state)
            print(curr_loop - loops[idx])
            break
        else:
            states.append(state)
            loops.append(curr_loop)

    return n_redist

inp = np.array([2,8,8,5,4,2,3,1,5,5,1,2,15,13,5,14])
# inp = np.array([0, 2, 7, 0])
print(main(inp))
