"""Models a network of pipelines."""

import collections


class PipelineSegment(object):
    """Models a segment of a pipeline network between two terminals."""

    def __init__(self, terminal_a, terminal_b):
        self.state = (terminal_a, terminal_b)

    terminal_a = property(lambda self: self.state[0])

    terminal_b = property(lambda self: self.state[1])


class PipelineNetwork(object):
    """Models a network of pipelines."""

    def __init__(self):
        """Construct an empty _ipeline network."""

        # Build a network using an adjacency representation
        self.network = collections.defaultdict(set)

    def add_segment(self, pipeline_segment):
        """Add `pipeline_segment` to this network."""
        self.network[pipeline_segment.terminal_a].add(pipeline_segment.terminal_b)
        self.network[pipeline_segment.terminal_b].add(pipeline_segment.terminal_a)

    def __repr__(self):
        """Return a string representation of myself."""
        return repr(self.network)
