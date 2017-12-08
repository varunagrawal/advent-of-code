import argparse
import numpy as np

class Node:
    def __init__(self, name, weight):
        self.weight = int(weight)
        self.name = name
        self.back_ptr = []
        self.subprograms = []
        self.total_weight = 0
        self.nodes = {}

    def __str__(self):
        return "{0} [{1}:{3}] - [{2}]".format(self.name, self.weight, self.subprograms, self.total_weight)


def parse_input(lines):
    programs = {}

    for line in lines:
        x = line.split(' ')
        node = Node(x[0], x[1].replace('(', '').replace(')', ''))

        if len(x) > 2:  # we have subprograms on top of this program
            for s in x[3:]:  # ignore the name, weight and pointer
                node.subprograms.append(s.replace(',', '').replace('\n', ''))

        programs[node.name] = node

    for k, node in programs.items():
        for p in node.subprograms:
            programs[p].back_ptr.append(node.name)

    return programs


def part1(programs):
    for _, p in programs.items():
        if len(p.back_ptr) == 0:
            print("Base program is: ", p.name)
            return p.name

def compute_total_weight(node, programs):
    if len(node.subprograms) == 0:
        node.total_weight = node.weight
        return node.total_weight

    else:
        if node.total_weight > 0:  # this means the total weight has already been assigned
            return node.total_weight
        else:
            # assuming we are guaranteed to have a DAG
            for s in node.subprograms:
                node.total_weight += compute_total_weight(programs[s], programs)
            node.total_weight += node.weight
            return node.total_weight

def construct_graph(programs, root_node="mwzaxaj"):
    root = programs[root_node]
    for s in root.subprograms:
        g = construct_graph(programs, root_node=s)
        root.nodes[s] = g

    return root

def find_unequal_weight(root):
    weights = []
    for k, node in root.nodes.items():
        # We need to find the lowest node in the tree aka bottom up
        # The difference percolates up
        find_unequal_weight(node)
        weights.append(node.total_weight)

    for i in range(len(weights)):
        if weights[i] != weights[(i+1)%len(weights)] \
            and weights[i] != weights[(i+2)%len(weights)]:
            for k in root.nodes:
                if root.nodes[k].total_weight == weights[i]:
                    print(k)
                    print(root.nodes[k].subprograms)
                    print("The unequal weight is: ", root.nodes[k].weight)
                    print("The correct weight should be: ", root.nodes[k].weight - (weights[i] - weights[(i+1)%len(weights)]))

                    # We found the first instace.
                    # everything else is a result of the difference propagating up the tree
                    exit(0)

def part2(programs, root):
    for _, p in programs.items():
        compute_total_weight(p, programs)

    g = construct_graph(programs, root_node=root)
    
    find_unequal_weight(g)
        

with open("day7.in", "r") as f:
    lines = f.readlines()

programs = parse_input(lines)

root = part1(programs)

part2(programs, root)