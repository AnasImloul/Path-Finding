from math import sqrt


class Node:
    def __init__(self, pos, neighbors=None):
        self.pos = pos
        if neighbors is not None:
            self.neighbors = neighbors
        else:
            self.neighbors = set()

    def add_neighbor(self, node):
        self.neighbors.add(node)
        node.neighbors.add(self)

    def distance(self, node):
        return sqrt(sum(pow(a - b, 2) for a, b in zip(self.pos, node.pos)))

    def __repr__(self):
        return f"Node({', '.join(self.pos)})"

    def __eq__(self, other):
        return self.pos == other.pos

    def __hash__(self):
        return hash(self.pos)

    def __getitem__(self, item):
        return self.pos[item]

    def __setitem__(self, key, value):
        self.pos[key] = value

    def __iter__(self):
        return iter(self.pos)