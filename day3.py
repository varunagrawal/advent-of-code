
"""Solution for day 3"""

def steps(x):
    i = 1
    while True:
        if x < i*i:
            break
        i += 2
    top_left = (i-1)*(i-1) + 1
    bottom_right = (i-2)*(i-2)
    top_right = bottom_right + (top_left - bottom_right) // 2
    bottom_left = top_left + (i*i - top_left) // 2

    print(bottom_right)
    if x == bottom_right:
        return i-2-1

    elif x == top_left:
        return i-1

    elif x == bottom_left or x == top_right:
        # same distance as top left corner due to symmetry
        return i-1

    elif x < top_right:
        if top_right - x < x - bottom_right:
            return i-1 - (top_right - x)
        elif top_right - x > x - bottom_right:
            return (i-1) - (x - bottom_right)
        else:
            return (i-1)//2

    elif x < top_left and x > top_right:
        if top_left - x < x - top_right:  # closer to top left
            return i - 1 - (top_left - x)
        elif top_left - x > x - top_right:
            return i - 1 - (x - top_right)
        else:
            return (i-1)//2
    elif x < bottom_left and x > top_left:
        if bottom_left - x < x - top_left:
            return i - 1 - (bottom_left - x)
        elif bottom_left - x > x - top_left:
            return i - 1 - (x - top_left)
        else:
            return (i-1)//2
    elif x > bottom_left:
        next = i*i
        if next - x < x - bottom_left:
            return i - 1 - (next-x)
        elif next - x > x - bottom_left:
            return i - 1 - (x - bottom_left)
        else:
            return (i-1)//2
    
def part1():
    tests = [(5, 2), (9, 2), (13, 4), (15, 2), (17, 4), (23, 2), (25, 4), (49, 6)]
    for t in tests:
        print(t[0], steps(t[0]), t[1])

    print(steps(312051))


def part2():
    pass
