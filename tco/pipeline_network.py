class PipelineNetwork(object):
    """Models a network of pipelines."""

    def __init__(self):
        pass

    def add_segment(self, terminal_a, terminal_b, cost=0):
        """Add a segment between terminal_a and terminal_b."""

    def is_connected(self, terminal_a, terminal_b):
        """Determine if terminal_a is connected to terminal_b."""
        return True

    def minimum_cost_route(self, terminal_a, terminal_b):
        """Calculate the minimum cost route between terminal_a and terminal_b."""
        return [], 0
