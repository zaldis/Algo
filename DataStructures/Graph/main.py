from collections import defaultdict


class UndirectedGraph:
    def __init__(self) -> None:
        self.adjacency_list = defaultdict(list)

    def connect_nodes(self, node_a: int, node_b: int) -> None:
        self.adjacency_list[node_a].append(node_b)
        self.adjacency_list[node_b].append(node_a)

    def has_edge(self, node_a: int, node_b: int) -> bool:
        return node_b in self.adjacency_list[node_a]


graph = UndirectedGraph()
assert not graph.has_edge(1, 5)

graph.connect_nodes(1, 5)
assert graph.has_edge(1, 5)

print("well done!")