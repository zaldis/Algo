from zaldisalgo.algos.search.short_path.dijkstra import DijkstraShortPathSearch
from zaldisalgo.algos.search.short_path.models import Edge


def test_general_case_with_relaxations() -> None:
    edges = [
        Edge(0, 1, 5),
        Edge(0, 2, 3),
        Edge(2, 1, 1),
        Edge(1, 3, 4),
        Edge(2, 4, 5),
        Edge(2, 3, 4)
    ]
    vstart = 0
    distances = DijkstraShortPathSearch(edges).short_paths(vstart)
    assert distances == {
        0: 0,
        1: 4,
        2: 3,
        3: 7,
        4: 8,
    }

