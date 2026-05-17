from dataclasses import dataclass


@dataclass
class Edge:
    start: int
    end: int
    cost: int


@dataclass
class MinSpanTree:
    edges: list[Edge]

    @property
    def cost(self) -> int:
        return sum([e.cost for e in self.edges])


def find_min_cost(number_of_vertices: int, edges: list[Edge]) -> MinSpanTree:
    graph = [[0] * number_of_vertices for _ in range(number_of_vertices)]
    for edge in edges:
        graph[edge.start][edge.end] = edge.cost
        graph[edge.end][edge.start] = edge.cost
    visited_vertices = {0}
    
    min_span_tree = MinSpanTree([])

    for join_step in range(number_of_vertices):
        min_cost_edge: Edge | None = None
        for edge in edges:
            if (
                edge.start in visited_vertices and edge.end not in visited_vertices
                or edge.start not in visited_vertices and edge.end in visited_vertices
            ):
                if min_cost_edge is None or min_cost_edge.cost > edge.cost:
                    min_cost_edge = edge
        if min_cost_edge:
            visited_vertices.add(min_cost_edge.start)
            visited_vertices.add(min_cost_edge.end)
            min_span_tree.edges.append(min_cost_edge)
    
    return min_span_tree


# graph_edges = [
#     Edge(0, 1, 5),
#     Edge(0, 2, 3),
#     Edge(1, 2, 1),
#     Edge(1, 3, 3),
#     Edge(2, 3, 4),
#     Edge(2, 4, 5)
# ]
# number_of_vertices = 5


graph_edges = [
    Edge(0, 1, 5),
    Edge(0, 2, 3),
    Edge(1, 2, 1),
    # Edge(1, 3, 3),
    # Edge(2, 3, 4),
    Edge(2, 4, 5)
]
number_of_vertices = 5


min_span_tree = find_min_cost(number_of_vertices, graph_edges)

if len(min_span_tree.edges) == number_of_vertices-1:
    print("All cities are connected!")
    for edge in min_span_tree.edges:
        print(f"{edge.start} <-{edge.cost}-> {edge.end}")

    print()
    print(f"Overall cost is {min_span_tree.cost}")
else:
    print("Cities can't be connected!")

