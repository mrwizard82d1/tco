import unittest

import tco


class TestGraph(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
