from zaldisalgo.ds import UndirectedGraph


def test_edge_which_does_not_exist():
    graph = UndirectedGraph()
    assert not graph.has_edge(1, 5)


def test_existed_edge():
    graph = UndirectedGraph()
    graph.connect_nodes(1, 5)
    assert graph.has_edge(1, 5)
