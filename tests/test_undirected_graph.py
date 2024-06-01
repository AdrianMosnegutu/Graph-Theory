import unittest
from src.graphs.undirected_graph import UndirectedGraph


class TestUndirectedGraph(unittest.TestCase):
    def setUp(self):
        self.graph = UndirectedGraph(5)

    def test_add_edge_to_graph(self):
        self.graph.add_edge((0, 1))
        self.assertEqual(self.graph.edges_count, 1)

    def test_add_existing_edge_raises_error(self):
        self.graph.add_edge((0, 1))
        with self.assertRaises(ValueError):
            self.graph.add_edge((0, 1))

    def test_remove_edge_from_graph(self):
        self.graph.add_edge((0, 1))
        self.graph.remove_edge((0, 1))
        self.assertEqual(self.graph.edges_count, 0)

    def test_remove_nonexistent_edge_raises_error(self):
        with self.assertRaises(ValueError):
            self.graph.remove_edge((0, 1))

    def test_add_vertex_to_graph(self):
        self.graph.add_vertex(5)
        self.assertEqual(self.graph.vertices_count, 6)

    def test_add_existing_vertex_raises_error(self):
        with self.assertRaises(ValueError):
            self.graph.add_vertex(0)

    def test_remove_vertex_from_graph(self):
        self.graph.add_vertex(5)
        self.graph.remove_vertex(5)
        self.assertEqual(self.graph.vertices_count, 5)

    def test_remove_nonexistent_vertex_raises_error(self):
        with self.assertRaises(ValueError):
            self.graph.remove_vertex(5)

    def test_are_connected_returns_true_when_connected(self):
        self.graph.add_edge((0, 1))
        self.assertTrue(self.graph.are_connected(0, 1))

    def test_are_connected_returns_false_when_not_connected(self):
        self.assertFalse(self.graph.are_connected(0, 1))

    def test_degree_returns_correct_degree(self):
        self.graph.add_edge((0, 1))
        self.graph.add_edge((0, 2))
        self.assertEqual(self.graph.degree(0), 2)

    def test_degree_raises_error_for_nonexistent_vertex(self):
        with self.assertRaises(ValueError):
            self.graph.degree(5)

    def test_neighbours_returns_correct_neighbours(self):
        self.graph.add_edge((0, 1))
        self.graph.add_edge((0, 2))
        self.assertEqual(list(self.graph.neighbours(0)), [1, 2])

    def test_neighbours_raises_error_for_nonexistent_vertex(self):
        with self.assertRaises(ValueError):
            list(self.graph.neighbours(5))


if __name__ == "__main__":
    unittest.main()