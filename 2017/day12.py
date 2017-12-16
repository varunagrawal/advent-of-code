def parse_graph(lines):
    graph = {}

    for line in lines:
        node, connections = line.split('<->')
        graph[node.strip()] = [x.strip() for x in connections.split(',')]
    return graph


def part1(input):
    graph = parse_graph(input)
    count = 0

    if '0' in graph.keys():
        count += 1
        visited = ['0']
        to_visit = graph['0']

        while len(to_visit) > 0:
            node = to_visit.pop(0)
            if node not in visited:
                visited.append(node)
                for n in graph[node]:
                    if n not in visited:
                        to_visit.append(n)
                
                # print(to_visit)
                count += 1
                # print(visited)
                
    print(count)

with open('day12.in', 'r') as f:
    input = f.readlines()

# part1(input)

def find_groups(k, groups, graph):
    # Check to see if k is already a part of a group
    for key in groups.keys():
        if k in groups[key]:
            return groups

    groups[k] = [k]

    to_visit = graph[k]
    
    while len(to_visit) > 0:
        node = to_visit.pop(0)
        if node not in groups[k]:
            groups[k].append(node)
            for n in graph[node]:
                if n not in groups[k]:
                    to_visit.append(n)
    return groups


def part2(input):
    graph = parse_graph(input)
    count = 0
    groups = {}

    for k in graph.keys():
        groups = find_groups(k, groups, graph)
    # print(groups)

    print(len(groups.keys()))

part2(input)