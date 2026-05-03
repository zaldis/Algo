from zaldisalgo.algos.search.short_path.bellman_ford import BellmanFordShortPathSearch
from zaldisalgo.algos.search.short_path.models import Edge


def test_positive_edges() -> None:
    edges = [
        Edge(0, 1, 5),
        Edge(0, 2, 3),
        Edge(2, 1, 1),
        Edge(1, 3, 4),
        Edge(2, 4, 5),
        Edge(2, 3, 4)
    ]
    vstart = 0
    distances = BellmanFordShortPathSearch(5, edges).short_paths(vstart)
    assert distances == [
        0, 4, 3, 7, 8, 
    ]


def test_negative_edges_without_negative_loop() -> None:
    edges = [
        Edge(0, 1, 5),
        Edge(0, 2, 3),
        Edge(2, 1, 1),
        Edge(1, 3, -4),
        Edge(2, 4, 5),
        Edge(2, 3, 4)
    ]
    vstart = 0
    distances = BellmanFordShortPathSearch(5, edges).short_paths(vstart)
    assert distances == [
        0, 4, 3, 0, 8, 
    ]
