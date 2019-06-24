from exceptions import ZeroOrNegativeWeightedEdgeException, WeightOutOfBoundsException

class Node:
    def __init__(self, label):
        self.adjacences = {}
        self.__visited = False
        self.__label = label

    def add_edge(self, node, w=1):
        if w <= 0:
            raise ZeroOrNegativeWeightedEdgeException
        
        if(node not in self.adjacences.keys()):
            self.adjacences[node] = 0
        self.adjacences[node] += w

    def has_adjacence(self):
        return self.adjacences != {}

    def exist_target_node(self, target_node) -> bool:
        if target_node in self.adjacences.keys():
            return True
        else:
            return False

    def get_adjacence_weight(self, target_node):
        if not self.exist_target_node(target_node):
            return 0
        return self.adjacences[target_node]

    def remove_edge(self, target_node, w=1) -> int:
        if w <= 0:
            raise ZeroOrNegativeWeightedEdgeException

        curr_edge_weight = self.get_adjacence_weight(target_node)

        if curr_edge_weight != 0:
            if w > curr_edge_weight:
                raise WeightOutOfBoundsException
            elif w == curr_edge_weight:
                self.adjacences.pop(target_node, None)
                return 0
            else:
                self.adjacences[target_node] -= w
                return self.adjacences[target_node]
        else:
            return 0

    def was_visited(self) -> bool:
        if self.__visited:
            return True
        else:
            return False

    def set_visited(self, visited: bool) -> None:
        self.__visited = visited

    def get_label(self) -> str:
        return self.__label

    def set_label(self, new_label: str) -> None:
        self.__label = new_label