import collections


class Graph(object):
    """Models simple undirected graph."""

    def __init__(self):
        """Construct an empty graph."""
        self.adjacencyList = collections.defaultdict(dict)

    def add_edge(self, u, v, weight=0):
        """Adds an edge between nodes u and v with optional weight."""
        self.adjacencyList[u][v] = weight
        self.adjacencyList[v][u] = weight

    def neighbors(self, u):
        """Returns the neighbors of node u."""
        return self.adjacencyList[u]
