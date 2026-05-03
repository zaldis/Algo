from zaldisalgo.algos.search.short_path.models import Edge
from zaldisalgo.algos.search.short_path.floyd_warshall import FloydWarshallShortPathSearch


def test_general_case_with_relaxation() -> None:
    edges = [
        Edge(0, 1, 5),
        Edge(0, 2, 3),
        Edge(2, 1, 1),
        Edge(1, 3, 4),
        Edge(2, 4, 5),
        Edge(2, 3, 4)
    ]
    distances = FloydWarshallShortPathSearch(6, edges).short_paths()
    inf = float('inf')
    assert distances == [
        [0, 4, 3, 7, 8, inf],
        [4, 0, 1, 4, 6, inf],
        [3, 1, 0, 4, 5, inf],
        [7, 4, 4, 0, 9, inf],
        [8, 6, 5, 9, 0, inf],
        [inf, inf, inf, inf, inf, 0]
    ]

