from collections import defaultdict


class UndirectedGraph:
    def __init__(self) -> None:
        self.adjacency_list = defaultdict(list)

    def connect_nodes(self, node_from: int, node_to: int) -> None:
        self.adjacency_list[node_from].append(node_to)
        self.adjacency_list[node_to].append(node_from)

    def has_edge(self, node_from: int, node_to: int) -> bool:
        return node_to in self.adjacency_list[node_from]
