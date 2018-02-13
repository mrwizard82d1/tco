import tco

class PipelineNetwork(object):
    """Models a network of pipelines."""

    def __init__(self):
        self.state = tco.Graph()

    def add_segment(self, terminal_a, terminal_b, toll=0):
        """Add a segment between terminal_a and terminal_b."""
        self.state.add_edge(terminal_a, terminal_b, weight=toll)

    def is_connected(self, terminal_a, terminal_b):
        """Determine if terminal_a is connected to terminal_b."""
        route = self.state.breadth_first_search(terminal_a, terminal_b)
        return True if route else False

    def minimum_cost_route(self, terminal_a, terminal_b):
        """Calculate the minimum cost route between terminal_a and terminal_b."""
        return [], 0
