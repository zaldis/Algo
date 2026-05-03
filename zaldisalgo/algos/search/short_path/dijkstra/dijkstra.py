import heapq

from ..models import Edge


class DijkstraShortPathSearch:
    def __init__(self, edges: list[Edge]) -> None:
        self._neighbours: dict[int, list[Edge]] = {}
        for edge in edges:
            if edge.start not in self._neighbours:
                self._neighbours[edge.start] = []
            if edge.end not in self._neighbours:
                self._neighbours[edge.end] = []
            self._neighbours[edge.start].append(edge)
            self._neighbours[edge.end].append(edge.reversed())

    def short_paths(self, vstart: int) -> dict[int, int]:
        distances: dict[int, int] = {}
        distances[vstart] = 0
        min_dist_vertex_heap = [(0, vstart)]
        while len(min_dist_vertex_heap):
            curr_cost, curr_vertex = heapq.heappop(min_dist_vertex_heap)
            neighbours = self._neighbours[curr_vertex]

            for edge in neighbours:
                alternative_cost = curr_cost + edge.cost
                if not edge.end in distances:
                    distances[edge.end] = alternative_cost
                    heapq.heappush(min_dist_vertex_heap, (alternative_cost, edge.end))
                else:
                    distances[edge.end] = min(alternative_cost, distances[edge.end])
        return distances

