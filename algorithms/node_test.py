import unittest

from node import Node

class NodeTest(unittest.TestCase):

    """
        NODE ADJACENCE TESTS:
        [1] Node has adjacence
        [2] Node hasn't adjacence
    """
    
    def test_node_has_no_adjacence(self):
        my_node = Node("MyNode")
        self.assertEqual(False, my_node.has_adjacence())

    def test_node_has_adjacence(self):
        my_node = Node("MyNode")
        my_node.add_edge(Node("TargetNode"))
        self.assertEqual(True, my_node.has_adjacence())

    """
        ADD EDGE TESTS:
        [1] Add edge with positive weight
        [2] Add edge with negative weight
        [3] Add edge with zero weight
        [4] Increase edge - Edge that already exist
    """

    def test_add_edge_with_weight_equal_2(self):
        my_node = Node("MyNode")
        target_node = Node("TargetNode")
        my_node.add_edge(target_node, 2)
        self.assertEqual(2, my_node.get_adjacence_weight(target_node))

    def test_add_edge_with_negative_weight(self):
        my_node = Node("MyNode")
        target_node = Node("TargetNode")
        
        with self.assertRaises(Exception):
            my_node.add_edge(target_node, -3)

    def test_add_edge_with_zero_weight(self):
        my_node = Node("MyNode")
        target_node = Node("TargetNode")

        with self.assertRaises(Exception):
            my_node.add_edge(target_node, 0)

    def test_increase_edge_weight_from_2_to_5(self):
        my_node = Node("MyNode")
        target_node = Node("TargetNode")
        my_node.add_edge(target_node, 2) # add 2 wheighted directed edge with target
        my_node.add_edge(target_node, 2) # with a edge already exist, increses the weight in 2 -> resulting 4
        self.assertEqual(4, my_node.get_adjacence_weight(target_node))


    """
        GET ADJACENCE WEIGHT TESTS:
        [1] Adjacence dont exist
    """
    def test_get_adjancence_weight_in_a_adjacence_that_dont_exist(self):
        my_node = Node("MyNode")
        target_node = Node("TargetNode")
        self.assertEqual(0, my_node.get_adjacence_weight(target_node))

    """
        REMOVE EDGE TESTS:
        [1] Positive weight
        [2] Positive weight with number more than the actual weight of the edge
        [3] Remove exacly the same weight of the edge
        [4] Negative weight
        [5] Zero weight
        [6] If target node doesn't exist
    """
    def test_remove_edge_with_positive_weight_removing_3_for_5_remaining_2(self):
        my_node = Node("MyNode")
        target_node = Node("TargetNode")
        my_node.add_edge(target_node, 5)
        remaining = my_node.remove_edge(target_node, 3)
        self.assertEqual(2, remaining)

    def test_remove_edge_with_positive_weight_more_than_the_actual_weeght_of_the_edge(self):
        my_node = Node("MyNode")
        target_node = Node("TargetNode")
        my_node.add_edge(target_node, 5)

        with self.assertRaises(Exception):
            my_node.remove_edge(target_node, 6) # the edge have weight of 5, but 6 was given

    def test_remove_edge_with_the_weight_exacly_the_same_as_the_actual_weight_of_th_edge(self):
        my_node = Node("MyNode")
        target_node = Node("TargetNode")
        my_node.add_edge(target_node, 5)
        remaining = my_node.remove_edge(target_node, 5)
        self.assertEqual(0, remaining)

    def test_remove_edge_with_negative_weight(self):
        my_node = Node("MyNode")
        target_node = Node("TargetNode")
        my_node.add_edge(target_node, 5)
        
        with self.assertRaises(Exception):
            my_node.remove_edge(target_node, -10)

    def test_remove_edge_with_weight_equal_zero(self):
        my_node = Node("MyNode")
        target_node = Node("TargetNode")
        my_node.add_edge(target_node, 5)

        with self.assertRaises(Exception):
            my_node.remove_edge(target_node, 0)

    def test_remove_edge_when_the_target_node_doest_exist(self): # return 0
        my_node = Node("MyNode")
        target_node = Node("TargetNode")
        self.assertEqual(0, my_node.remove_edge(target_node, 5))

    """
        VISIT TESTS:
        [1] Node was visited? -> True
        [2] Node was visited? -> False
    """

    def test_node_was_visited_returning_false(self):
        my_node = Node("MyNode")
        self.assertEqual(False, my_node.was_visited())

    def test_node_was_visited_returning_true(self):
        my_node = Node("MyNode")
        my_node.set_visited(True)
        self.assertEqual(True, my_node.was_visited())


# if __name__ == "__main__":
#      unittest.main()