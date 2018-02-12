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

    @staticmethod
    def construct_path(target, paths_to_source):
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
                return self.construct_path(v, travel_log)

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


