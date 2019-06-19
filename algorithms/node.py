
class Node:
    def __init__(self, label: str):
        self._label = label
        self._visited = False
        self._adjacences = []

    def add_adj(dest_node: Node) -> None:
        self._adjacences.append(dest_node)

    def remove_adj(dest_node: Node) -> None:
        if dest_node not in self._adjacences:
            self._adjacences.remove(dest_node)

    def has_visited() -> bool:
        if not self._visited:
            self._visited = True
            return True
        return False