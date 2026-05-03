from ..models import Edge


class BellmanFordShortPathSearch:
    def __init__(self, amount_of_vertices: int, edges: list[Edge]) -> None:
        self._n = amount_of_vertices
        self._edges = edges

    def short_paths(self, start: int) -> list[float]:
        _costs = [float('inf')] * self._n
        _costs[start] = 0
        for _ in range(self._n):
            for edge in self._edges:
                if _costs[edge.start] < float('inf'):
                    _costs[edge.end] = min(
                        _costs[edge.end],
                        _costs[edge.start] + edge.cost
                    )
        return _costs

