import unittest

from node import Node
from graph import Graph

class GraphTest(unittest.TestCase):

    """
        ADD VERTICES TESTS:
        [1] Add vertice - OK
        [2] Add a non vertice (no instance of Node) - OK
        [3] Add a vertice that already is in the graph - OK
        [4] Add vertice, if the graph dont have a root, give to him - OK
    """
    def test_add_vertice(self):
        my_node = Node("MyNode")
        g = Graph()
        g.add_vertice(my_node)
        self.assertEqual(True, g.has_vertice(my_node))

    def test_add_a_non_vertice(self):
        g = Graph()
        non_vertice = 1234 # no instance of Node
        with self.assertRaises(Exception):
            g.add_vertice(non_vertice)

    def test_add_vertice_that_already_is_in_the_graph(self):
        my_node = Node("MyNode")
        g = Graph()
        g.add_vertice(my_node)
        with self.assertRaises(Exception):
            g.add_vertice(my_node) # add the same vertice

    def test_add_the_first_vertice_of_the_graph_and_turn_into_root(self):
        my_node = Node("MyNode")
        my_node2 = Node("MyNode")
        g = Graph()
        g.add_vertice(my_node)
        g.add_vertice(my_node2)
        self.assertEqual(my_node, g.get_root())