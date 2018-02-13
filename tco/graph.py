import collections
import sys


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

    def nodes(self):
        """Return all the nodes in this graph."""
        return set(self.adjacencyList.keys())

    @staticmethod
    def construct_search_path(target, paths_to_source):
        """Construct the path from source to target using paths_to_source."""
        path = [target]
        while True:
            reverse_edge = paths_to_source[target]
            if reverse_edge != (None, None):
                target = reverse_edge[0]
                path.append(target)
            else:
                break

        path.reverse()
        return path

    def breadth_first_search(self, u, v):
        """Perform a breadth first search from node u to v."""
        to_visit = collections.deque()
        visited = set()
        travel_log = {}  # keys are nodes; values are reverse edges

        start = u
        travel_log[u] = (None, None)

        to_visit.append(start)
        while to_visit:
            from_node = to_visit.popleft()
            if from_node == v:
                return self.construct_search_path(v, travel_log)

            for to_node in self.neighbors(from_node).keys():
                if to_node in visited:
                    continue

                if to_node not in to_visit:
                    # avoid loops
                    travel_log[to_node] = (from_node, to_node)
                    to_visit.append(to_node)

            visited.add(from_node)

        # visited all nodes but failed to find target
        return []

    @staticmethod
    def to_visit_closest_to_source(to_visit, distances_to_source):
        """Return a node to be visited that is closest to the source node."""
        return min(to_visit, key=lambda n: distances_to_source[n])

    @staticmethod
    def construct_shortest_path(target, paths_to_source):
        """Return the shortest path from source to target using paths_to_source."""
        u = target
        target_to_source = [u]
        while paths_to_source[u]:
            target_to_source.append(paths_to_source[u])
            u = paths_to_source[u]

        return list(reversed(target_to_source))

    def shortest_path(self, source, target, infinity=sys.maxsize):
        """Return the lowest cost path from source to target using Dijkstra's algorithm.

        The additional parameter, infinity, allows callers to specify a largest possible distance appropriate to their
        problem. This parameter is necessary because python(3) no longer supports `sys.maxint`. The default value is
        `sys.maxsize`. This value is a practical limit, but not actually a limit for python 3 integers. See
        https://stackoverflow.com/questions/13795758/what-is-sys-maxint-in-python-3 for details.
        """

        to_visit = set()
        distances_to_source = {}
        paths_to_source = {}

        for v in self.nodes():
            distances_to_source[v] = infinity
            paths_to_source[v] = None
            to_visit.add(v)
        distances_to_source[source] = 0  # fix distance of source from source

        while to_visit:
            u = self.to_visit_closest_to_source(to_visit, distances_to_source)

            to_visit.remove(u)
            if u == target:
                if paths_to_source[target]:
                    return self.construct_shortest_path(target, paths_to_source), distances_to_source[target]
                return None

            for v in self.neighbors(u):
                candidate = distances_to_source[u] + self.adjacencyList[u][v]
                if candidate < distances_to_source[v]:
                    # if we found a sorter path to the source, update distances and paths
                    distances_to_source[v] = candidate
                    paths_to_source[v] = u

        return None
