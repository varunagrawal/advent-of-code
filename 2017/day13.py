import itertools


class Layer:
    def __init__(self, depth, range):
        self.depth = depth
        self.range = range
        self.direction = 1
        self.pos = 0

    def step(self):
        self.pos = self.pos + self.direction

        # if the scanner position is 0 or max, we change directions
        if self.pos == 0 or self.pos == self.range-1:
            self.direction *= -1
    
    def __str__(self):
        repr = ""
        for i in range(self.range):
            if i == self.pos:
                cell = "[s]"
            else:
                cell = "[]"
            repr += cell

        return "{0}: {1}".format(self.depth, repr)

def parse_input(input_file):
    with open(input_file, 'r') as f:
        x = f.readlines()

    recording = {}
    for i in x:
        depth, range = i.split(':')
        recording[int(depth.strip())] = int(range.strip())

    return recording


def part1(recording):
    layers = []
    for d, r in recording.items():
        layers.append(Layer(d, r))

    max_layer = max(list(recording.keys()))

    severity = 0

    for i in range(max_layer+1):
        # print("Step: ", i)
        for l in layers:
            # print(l)
            if l.depth == i and l.pos == 0:
                severity += (l.depth * l.range)
            l.step()
        # print(severity)
        # print()
    
    print(severity)


def scanner(height, time):
    """Fast way to get the position of the scanner at time `time`"""
    offset = time % ((height - 1) * 2)  # 2(height-1) is the number of steps from top to bottom
    return 2*(height-1)-offset if offset > height else offset

def part2(recording):
    max_layer = max(list(recording.keys()))
    wait = 0
    for wait in itertools.count():
        caught = 0
        for l in recording:
            if scanner(recording[l], wait + l) == 0:
                caught += 1
        if caught == 0:
            print("We have to wait for ", wait)
            break

recording = parse_input("day13.in")
part1(recording)
part2(recording)