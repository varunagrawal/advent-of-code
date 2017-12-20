class Particle:
    def __init__(self, pos: list, vel: list, acc: list):
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def step(self):
        for i in range(len(self.pos)):
            self.vel[i] += self.acc[i]
            self.pos[i] += self.vel[i]
        
    def distance(self):
        dist = 0
        for i in range(len(self.pos)):
            dist += abs(self.pos[i])
        return dist


def parse_tuple(t):
    t = t.split('=')[-1]
    data = t.strip()[1:-1]  # remove the '<>'
    # print(data)
    data = [int(x) for x in data.split(',')]
    return data

def parse_data(data):
    particle_data = []
    for i in data:
        d = i.split(', ')
        pos = parse_tuple(d[0])
        vel = parse_tuple(d[1])
        acc = parse_tuple(d[2])
        particle_data.append([pos, vel, acc])
    return particle_data 

def part1(particle_data):
    particles = []
    for d in particle_data:
        p = Particle(*d)
        particles.append(p)

    for _ in range(1000):
        min_dist = None
        min_part = None

        for i in range(len(particles)):
            particles[i].step()
            dist = particles[i].distance()

            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_part = i
    
        # print(min_dist)

    print(min_part)

def part2(particle_data):
    particles = []
    valid = []
    for d in particle_data:
        p = Particle(*d)
        particles.append(p)
        valid.append(True)

    for iter in range(1000):
        print(iter)
        min_dist = None
        min_part = None
        locs = []
        parts = []  # store the particle number for the location

        for i in range(len(particles)):
            if valid[i]:
                particles[i].step()
            dist = particles[i].distance()

            if particles[i].pos in locs:
                valid[i] = False
                idx = locs.index(particles[i].pos)
                valid[parts[idx]] = False
            else:
                locs.append(particles[i].pos)
                parts.append(i)

            if min_dist is None or dist < min_dist:
                min_dist = dist
                min_part = i
    
        # print(min_dist)

    print(sum([int(x) for x in valid]))

with open('day20.in', 'r') as f:
    data = f.readlines()

particle_data = parse_data(data)
# part1(particle_data)
part2(particle_data)
