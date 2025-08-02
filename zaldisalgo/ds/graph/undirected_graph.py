from collections import defaultdict


class UndirectedGraph[T]:
    def __init__(self) -> None:
        self.adjacency_list: dict[T, list[T]] = defaultdict(list)
        self.vertices = set()
        self.edges_count = 0

    def connect_nodes(self, node_from: T, node_to: T) -> None:
        """Connect two nodes"""
        self.adjacency_list[node_from].append(node_to)
        self.adjacency_list[node_to].append(node_from)
        self.vertices.add(node_from)
        self.vertices.add(node_to)
        self.edges_count += 1

    def has_edge(self, node_from: T, node_to: T) -> bool:
        """Check if two nodes are connected"""
        return node_to in self.adjacency_list[node_from]

    def __str__(self):
        return f"<UndirectedGraph | vertices={len(self.vertices)} edges={self.edges_count}>"


if __name__ == '__main__':
    # Create empty graph
    graph = UndirectedGraph[int]()
    print(f"Created empty graph {graph}")

    # Connect two nodes
    node1 = 5
    node2 = 10
    graph.connect_nodes(node1, node2)
    print("Added new edge 5 <-> 10.")
    print(graph)

    # Check the edge
    assert graph.has_edge(node1, node2)