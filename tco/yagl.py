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

        path = [node]

        while True:
            edge = meta[node]
            if edge != (None, None):
                node = edge[0]
                path.append(node)
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

    @staticmethod
    def to_visit_closest_to_source(to_visit, dists_to_source):
        """Return a node to be visited that is closest to the source node."""
        return min(to_visit, key=lambda n: dists_to_source[n])

    @staticmethod
    def shortest_path(source, target, paths_to_source):
        """Return the shortest path from source to target using paths_to_source."""
        u = target
        target_to_source = [u]
        while paths_to_source[u]:
            target_to_source.append(paths_to_source[u])
            u = paths_to_source[u]

        return list(reversed(target_to_source))

    def dijkstra(self, source, target, infinity=sys.maxsize):
        """Return the lowest cost path from source to target using Dijkstra's algorithm.

        The additional parameter, infinity, allows callers to specify a largest possible distance appropriate to their
        problem. This parameter is necessary because python(3) no longer supports `sys.maxint`. The default value is
        `sys.maxsize`. This value is a practical limit, but not actually a limit for python 3 integers. See
        https://stackoverflow.com/questions/13795758/what-is-sys-maxint-in-python-3 for details.
        """

        to_visit = set()
        dists_to_source = {}
        paths_to_source = {}

        for v in self.nodes():
            dists_to_source[v] = infinity
            paths_to_source[v] = None
            to_visit.add(v)
        dists_to_source[source] = 0  # fix distance of source from source

        while to_visit:
            u = self.to_visit_closest_to_source(to_visit, dists_to_source)

            to_visit.remove(u)
            if u == target:
                if paths_to_source[target]:
                    return self.shortest_path(source, target, paths_to_source), dists_to_source[target]
                return None

            for v in self.neighbors(u):
                candidate = dists_to_source[u] + self.adjList[u][v]
                if candidate < dists_to_source[v]:
                    # if we found a sorter path to the source, update distances and paths
                    dists_to_source[v] = candidate
                    paths_to_source[v]= u

        return None
