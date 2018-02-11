"""Yet another graph library."""

import collections


class Graph(object):
    """An undirected graph."""

    def __init__(self):
        """Construct an empty instance."""

        self.adjList = collections.defaultdict(set)

    def __repr__(self):
        return repr(self.adjList)

    def add_node(self, u):
        """Add the node, `u`"""
        self.adjList[u] = set()

    def add_edge(self, u, v):
        """Add the edges between nodes u and v."""

        self.adjList[u].add(v)
        self.adjList[v].add(u)

    def neighbors(self, u):
        return set(self.adjList[u])

    @staticmethod
    def construct_path(node, meta):
        """Construct a path from `node` using `meta`."""

        path = []

        while True:
            edge = meta[node]
            if edge != (None, None):
                node = edge[0]
                path.append(edge)
            else:
                break

        path.reverse()
        return path

    def bfs(self, source, target):
        """Perform a breadth-first search from `source` to `target`."""

        to_visit = collections.deque()
        visited = set()
        meta = {}  # dictionary keyed by starting node of edge and containing the edge from start to neighbor

        start = source
        meta[start] = (None, None)

        to_visit.append(start)

        while to_visit:
            from_node = to_visit.popleft()
            if from_node == target:
                return self.construct_path(target, meta)

            for to_node in self.neighbors(from_node):
                if to_node in visited:
                    continue

                if to_node not in to_visit:
                    meta[to_node] = (from_node, to_node)
                    to_visit.append(to_node)

            visited.add(from_node)
