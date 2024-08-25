from zaldisalgo.algos.search import RangeMinimumQuery


def test_get_query_on_single_value():
    rmq = RangeMinimumQuery([1])
    assert rmq.get_minimum_value(0, 0) == 1


def test_update_query_on_single_value():
    rmq = RangeMinimumQuery([1])
    rmq.update_value(0, 5)
    assert rmq.get_minimum_value(0, 0) == 5


def test_get_query_on_positive_values():
    rmq = RangeMinimumQuery([1, 5, 2, 4, 3])
    assert rmq.get_minimum_value(0, 4) == 1


def test_update_query_on_positive_values():
    rmq = RangeMinimumQuery([1, 5, 2, 4, 3])
    rmq.update_value(2, 6)
    assert rmq.get_minimum_value(2, 4) == 3


def test_get_query_on_negative_values():
    rmq = RangeMinimumQuery([1, -1, 5, 8, 3, 2, 0, 7])
    assert rmq.get_minimum_value(0, 7) == -1


def test_update_query_on_negative_values():
    rmq = RangeMinimumQuery([1, -1, 5, 8, 3, 2, 0, 7])
    rmq.update_value(1, 10)
    assert rmq.get_minimum_value(0, 7) == 0


def test_get_query_on_partial_binary_tree():
    rmq = RangeMinimumQuery([1, -1, 5, 8, 3, 2])
    assert rmq.get_minimum_value(0, 5) == -1
