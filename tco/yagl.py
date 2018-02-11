"""Yet another graph library."""

import collections
import sys


class Graph(object):
    """An undirected graph."""

    def __init__(self):
        """Construct an empty instance."""

        self.adjList = collections.defaultdict(dict)

    def __repr__(self):
        return repr(self.adjList)

    def add_node(self, u):
        """Add the node u"""
        self.adjList[u] = dict()

    def add_edge(self, u, v, weight=0):
        """Add the edges between nodes u and v with an optional weight."""

        self.adjList[u][v] = weight
        self.adjList[v][u] = weight

    def neighbors(self, u):
        """Return the neighbors of u."""
        return set(self.adjList[u].keys())

    def nodes(self):
        """Return all the nodes in this graph."""
        return set(self.adjList.keys())

    @staticmethod
    def construct_path(node, meta):
        """Construct a path from node using meta."""

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
        """Perform a breadth-first search from source to target."""

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

    def dijkstra(self, source, target, infinity=sys.maxsize):
        """Return the lowest cost path from source to target using Dijkstra's algorithm.

        The additional parameter, infinity, allows callers to specify a largest possible distance appropriate to their
        problem. This parameter is necessary because python(3) no longer supports `sys.maxint`. The default value is
        `sys.maxsize`. This value is a practical limit, but not actually a limit for python 3 integers. See
        https://stackoverflow.com/questions/13795758/what-is-sys-maxint-in-python-3 for details.
        """

        def to_visit_closest_to_source(to_visit):
            """Return a node to be visited that is closest to the source node."""
            return min(to_visit, key=lambda n: to_visit[n])

        weighted_nodes_to_visit = {source: 0}  # the nodes to visit "weighted" by their distance from the source node
        paths_to_source = collections.defaultdict(list)

        for v in self.nodes():
            if v != source:
                weighted_nodes_to_visit[v] = infinity
                paths_to_source[v] = None

        print('weighted_nodes_to_visit={}'.format(weighted_nodes_to_visit))
        print('paths_to_source={}'.format(paths_to_source))

        while weighted_nodes_to_visit:
            u = to_visit_closest_to_source(weighted_nodes_to_visit)
            print('node to visit={}'.format(u))

            del weighted_nodes_to_visit[u]

            print('weighted_nodes_to_visit={}'.format(weighted_nodes_to_visit))
            print('paths_to_source={}'.format(paths_to_source))

            if u == 'mid':
                break
