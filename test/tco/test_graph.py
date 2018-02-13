import unittest

import tco


class TestGraph(unittest.TestCase):
    """Test basic properties of the Graph class."""

    def test_add_edge_first_node_of_edge_has_second_node_as_single_neighbor(self):
        sut = tco.Graph()
        sut.add_edge(1, 2)

        self.assertEqual(sut.neighbors(1).keys(), {2})

    def test_add_edge_second_node_of_edge_has_first_node_as_single_neighbor(self):
        sut = tco.Graph()
        sut.add_edge(1, 2)

        self.assertEqual(sut.neighbors(2).keys(), {1})

    def test_add_edge_with_weight_edge_has_weight(self):
        sut = tco.Graph()
        sut.add_edge(1, 2, weight=2.71)

        self.assertEqual(sut.neighbors(1), {2: 2.71})


class TestGraphSearch(unittest.TestCase):
    """Test searching the Graph."""

    def test_empty_graph_breadth_first_search_is_empty(self):
        sut = tco.Graph()

        self.assertEqual(sut.breadth_first_search('a', 'b'), [])

    def test_single_edge_graph_breadth_first_search_first_to_another_is_empty(self):
        sut = tco.Graph()
        sut.add_edge('a', 'b')

        self.assertEqual(sut.breadth_first_search('a', 'c'), [])

    def test_single_edge_graph_breadth_first_search_first_to_second_returns_first_to_second_path(self):
        sut = tco.Graph()
        sut.add_edge('a', 'b')

        self.assertEqual(sut.breadth_first_search('a', 'b'), ['a', 'b'])


class TestGraphPath(unittest.TestCase):
    """Test finding paths through the Graph."""

    def test_empty_graph_dijkstra_is_none(self):
        sut = tco.Graph()

        self.assertEqual(sut.shortest_path('a', 'b'), None)

    def test_single_edge_graph_shortest_path_first_to_another_is_none(self):
        sut = tco.Graph()
        sut.add_edge('a', 'b')

        self.assertEqual(sut.shortest_path('a', 'c'), None)

    def test_single_edge_graph_shortest_path_first_to_second_returns_first_to_second_path(self):
        sut = tco.Graph()
        sut.add_edge('a', 'b')

        self.assertEqual(sut.shortest_path('a', 'b')[0], ['a', 'b'])

    def test_single_edge_graph_shortest_path_first_to_second_returns_first_to_second_weight(self):
        sut = tco.Graph()
        sut.add_edge('a', 'b', weight=3)

        self.assertEqual(sut.shortest_path('a', 'b')[1], 3)

    def test_multiple_edge_graph_shortest_path_returns_shortest_path_and_cost(self):
        sut = tco.Graph()
        sut.add_edge('a', 'b', weight=3)
        sut.add_edge('b', 'd', weight=3)
        sut.add_edge('a', 'c', weight=4)
        sut.add_edge('c', 'd', weight=3)
        sut.add_edge('a', 'd', weight=7)

        self.assertEqual(sut.shortest_path('a', 'd'), (['a', 'b', 'd'], 6))


if __name__ == '__main__':
    unittest.main()
