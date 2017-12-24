def parse_components(data):
    components = []

    for d in data:
        a, b = d.split('/')
        components.append((int(a), int(b)))

    return components

def solve(root, components, strength, length, part2=False):
    port = root[1]
    best_strength = strength
    longest_strength = strength

    longest = length

    is_leaf = True

    for c in components:
        comps = list(components)
        s = 0
        l = 0

        if c[0] == port:
            is_leaf = False
            comp = tuple(c)    
            comps.remove(c)
            s, l = solve(comp, comps, strength+sum(c), length+1, part2)
        elif c[1] == port:
            is_leaf = False
            comp = (c[1], c[0])
            comps.remove(c)
            s, l = solve(comp, comps, strength+sum(c), length+1, part2)
        
        best_strength = max(best_strength, s)
    
        # check if the chain is the longest and also has greater strength
        if l >= longest and s > longest_strength:
            longest = l
            longest_strength = s

    if part2:
        return longest_strength, longest

    return best_strength, 1

with open("day24.in", 'r') as f:
    data = f.readlines()

components = parse_components(data)
ans = solve((0, 0), components, 0, 1, part2=True)
print(ans)
