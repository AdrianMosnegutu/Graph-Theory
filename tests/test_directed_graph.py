from unittest import TestCase
from src.graphs.directed_graph import DirectedGraph


class TestDirectedGraph(TestCase):
    def setUp(self):
        self.graph = DirectedGraph(3)

    def tearDown(self):
        del self.graph

    def test_vertices_count(self):
        self.assertEqual(self.graph.vertices_count, 3)

    def test_edges_count(self):
        self.assertEqual(self.graph.edges_count, 0)

        self.graph.add_edge((0, 1), 1)
        self.assertEqual(self.graph.edges_count, 1)

    def test_vertices(self):
        self.assertEqual(list(self.graph.vertices), [0, 1, 2])

    def test_edges(self):
        self.graph.add_edge((0, 1), 1)
        self.assertEqual(list(self.graph.edges), [(0, 1)])

    def test_add_edge(self):
        self.graph.add_edge((0, 1), 1)
        self.assertTrue(self.graph.are_connected(0, 1))

        self.assertTrue(1 in self.graph.outbound_neighbours(0))
        self.assertTrue(0 in self.graph.inbound_neighbours(1))

        self.assertRaises(ValueError, self.graph.add_edge, (0, 1), 1)
        self.assertRaises(ValueError, self.graph.add_edge, (0, 4), 1)

    def test_remove_edge(self):
        self.graph.add_edge((0, 1), 1)
        self.assertTrue(self.graph.are_connected(0, 1))

        self.graph.remove_edge((0, 1))
        self.assertFalse(self.graph.are_connected(0, 1))

        self.assertRaises(ValueError, self.graph.remove_edge, (0, 1))
        self.assertRaises(ValueError, self.graph.remove_edge, (0, 4))

    def test_add_vertex(self):
        self.graph.add_vertex(10)
        self.assertEqual(self.graph.vertices_count, 4)
        self.assertRaises(ValueError, self.graph.add_vertex, 10)

    def test_remove_vertex(self):
        self.graph.add_edge((0, 1), 1)
        self.graph.add_edge((1, 2), 1)

        self.assertTrue(self.graph.are_connected(0, 1))
        self.assertTrue(self.graph.are_connected(1, 2))

        self.graph.remove_vertex(1)

        self.assertFalse(self.graph.are_connected(0, 1))
        self.assertFalse(self.graph.are_connected(1, 2))

        self.assertRaises(ValueError, self.graph.remove_vertex, 1)
        self.assertRaises(ValueError, self.graph.remove_vertex, 10)

    def test_are_connected(self):
        self.graph.add_edge((0, 1), 1)
        self.assertTrue(self.graph.are_connected(0, 1))
        self.assertFalse(self.graph.are_connected(1, 0))
        self.assertFalse(self.graph.are_connected(0, 2))
        self.assertFalse(self.graph.are_connected(1, 2))
        self.assertFalse(self.graph.are_connected(0, 4))

    def test_in_degree(self):
        self.graph.add_edge((0, 1), 1)
        self.graph.add_edge((1, 2), 1)

        self.assertEqual(self.graph.in_degree(0), 0)
        self.assertEqual(self.graph.in_degree(1), 1)
        self.assertEqual(self.graph.in_degree(2), 1)

        self.assertRaises(ValueError, self.graph.in_degree, 4)

    def test_out_degree(self):
        self.graph.add_edge((0, 1), 1)
        self.graph.add_edge((1, 2), 1)

        self.assertEqual(self.graph.out_degree(0), 1)
        self.assertEqual(self.graph.out_degree(1), 1)
        self.assertEqual(self.graph.out_degree(2), 0)

        self.assertRaises(ValueError, self.graph.out_degree, 4)

    def test_inbound_neighbours(self):
        self.graph.add_edge((0, 1), 1)
        self.assertEqual(list(self.graph.inbound_neighbours(0)), [])
        self.assertEqual(list(self.graph.inbound_neighbours(1)), [0])
        self.assertRaises(ValueError, self.graph.inbound_neighbours, 4)

    def test_outbound_neighbours(self):
        self.graph.add_edge((0, 1), 1)
        self.assertEqual(list(self.graph.outbound_neighbours(0)), [1])
        self.assertEqual(list(self.graph.outbound_neighbours(1)), [])
        self.assertRaises(ValueError, self.graph.outbound_neighbours, 4)

    def test_get_cost(self):
        self.graph.add_edge((0, 1), 1)
        self.assertEqual(self.graph.get_cost((0, 1)), 1)
        self.assertRaises(ValueError, self.graph.get_cost, (0, 4))

    def test_set_cost(self):
        self.graph.add_edge((0, 1), 1)
        self.graph.set_cost((0, 1), 2)

        self.assertEqual(self.graph.get_cost((0, 1)), 2)
        self.assertRaises(ValueError, self.graph.set_cost, (0, 4), 2)

    def test_copy(self):
        copy: DirectedGraph = self.graph.copy()

        copy.add_edge((0, 1), 1)
        copy.add_edge((1, 2), 1)

        self.assertEqual(copy.vertices_count, 3)

        self.assertTrue(copy.are_connected(0, 1))
        self.assertTrue(copy.are_connected(1, 2))

        self.assertFalse(self.graph.are_connected(0, 1))
        self.assertFalse(self.graph.are_connected(1, 2))
