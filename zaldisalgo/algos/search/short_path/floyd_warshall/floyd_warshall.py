from ..models import Edge


class FloydWarshallShortPathSearch:
    def __init__(self, amount_of_vertices: int, edges: list[Edge]) -> None:
        self._n = amount_of_vertices
        self._costs: list[list[float]] = [[float('inf')] * self._n for _ in range(self._n)]
        for v in range(self._n):
            self._costs[v][v] = 0
        for edge in edges:
            self._costs[edge.start][edge.end] = edge.cost
            self._costs[edge.end][edge.start] = edge.cost

    def short_paths(self) -> list[list[float]]:
        for k in range(self._n):
            for i in range(self._n):
                for j in range(self._n):
                    path_a = self._costs[i][k]
                    path_b = self._costs[k][j]
                    self._costs[i][j] = min(self._costs[i][j], path_a + path_b)
        return self._costs

