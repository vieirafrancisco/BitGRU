from node import Node

class Graph:
    """
        Graph is a pair G = (V, E), where V is a set of vertices and
        E is a set of two-sets with two distinct vertices, that we call edge.
        Directed Graph are graph in which edges have orientations.
    """
    def __init__(self):
        self.__root = None
        self.__vertices = []

    def add_vertice(self, vertice):
        if not isinstance(vertice, Node):
            raise Exception("Vertice parameter need to be a Node instance!")
        if self.has_vertice(vertice):
            raise Exception("This vertice aleady exist in the graph!")
        if not self.__root:
            self.__root = vertice
        self.__vertices.append(vertice)

        for child in vertice.adjacences:
            self.add_vertice(child) 

    def has_vertice(self, vertice):
        if vertice in self.__vertices:
            return True
        else:
            return False

    def get_root(self):
        return self.__root

    def update_graph(self, vertice, stack):
        vertice.set_visited(True)
        stack.append(vertice)

        for adjacent in vertice.adjacences:
            if adjacent.was_visited() and adjacent in stack:
                idx = stack.index(adjacent)
                m = stack[idx]
                for element in stack[idx+1:]:
                    if element < m:
                        m = element
                for element in stack:
                    element.remove_edge(adjacent, m)
            else:
                self.update_graph(adjacent, stack)

        stack.pop(vertice)
