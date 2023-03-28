from Node import Node
from queue import Queue


class Graph:
    def __init__(self, grid=None):
        self.nodes = dict()
        if grid is not None:
            self.build(grid)

    def add(self, pos):
        self.nodes[pos] = Node(pos)

    def add_neighbor(self, pos1, pos2):
        if pos1 not in self.nodes:
            self.add(pos1)

        if pos2 not in self.nodes:
            self.add(pos2)

        self.nodes[pos1].neighbors.add(self.nodes[pos2])
        self.nodes[pos2].neighbors.add(self.nodes[pos1])

    def build(self, matrix):
        n, m = matrix.shape
        steps = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for x in range(m):
            for y in range(n):

                if not matrix[y, x]:
                    continue

                self.add((x, y))
                for dx, dy in steps:
                    if not (0 <= x + dx < m and 0 <= y + dy < n):
                        continue

                    if not matrix[y + dy, x + dx]:
                        continue

                    self.add_neighbor((x, y), (x + dx, y + dy))


    def BFS(self, start, end):
        if start not in self.nodes or end not in self.nodes:
            return None

        queue = Queue()
        queue.put(start)
        parent = {start: None}

        while not queue.empty():
            current = queue.get()
            node = self.nodes[current]

            if current == end:
                break

            for neighbor in node.neighbors:
                if neighbor.pos not in parent:
                    parent[neighbor.pos] = current
                    queue.put(neighbor.pos)

        if end not in parent:
            return None

        path = []
        while end is not None:
            path.append(self.nodes[end])
            end = parent[end]

        path.reverse()

        return path

    def djikstra(self, start, end):
        if start not in self.nodes or end not in self.nodes:
            return None

        queue = Queue()
        queue.put(start)
        parent = {start: None}
        distance = {start: 0}

        while not queue.empty():
            current = queue.get()
            node = self.nodes[current]

            if current == end:
                break

            for neighbor in node.neighbors:
                if neighbor.pos not in parent:
                    parent[neighbor.pos] = current
                    distance[neighbor.pos] = distance[current] + node.distance(neighbor)
                    queue.put(neighbor.pos)

                elif distance[current] + node.distance(neighbor) < distance[neighbor.pos]:
                    parent[neighbor.pos] = current
                    distance[neighbor.pos] = distance[current] + node.distance(neighbor)
                    queue.put(neighbor.pos)

        if end not in parent:
            return None

        path = []
        while end is not None:
            path.append(self.nodes[end])
            end = parent[end]

        path.reverse()

        return path

    def a_star(self, start, end):
        if start not in self.nodes or end not in self.nodes:
            return None

        queue = Queue()
        queue.put(start)
        parent = {start: None}
        distance = {start: 0}
        cost = {start: self.nodes[start].distance(self.nodes[end])}

        while not queue.empty():
            current = queue.get()
            node = self.nodes[current]

            if current == end:
                break

            for neighbor in node.neighbors:
                if neighbor.pos not in parent:
                    parent[neighbor.pos] = current
                    distance[neighbor.pos] = distance[current] + node.distance(neighbor)
                    cost[neighbor.pos] = distance[neighbor.pos] + neighbor.distance(self.nodes[end])
                    queue.put(neighbor.pos)

                elif distance[current] + node.distance(neighbor) < distance[neighbor.pos]:
                    parent[neighbor.pos] = current
                    distance[neighbor.pos] = distance[current] + node.distance(neighbor)
                    cost[neighbor.pos] = distance[neighbor.pos] + neighbor.distance(self.nodes[end])
                    queue.put(neighbor.pos)

        if end not in parent:
            return None

        path = []
        while end is not None:
            path.append(self.nodes[end])
            end = parent[end]

        path.reverse()

        return path

    def cost(self, path):
        return sum(self.nodes[path[i]].distance(self.nodes[path[i + 1]]) for i in range(len(path) - 1))


