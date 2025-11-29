from zaldisalgo.algos.sort import timsort


def test_empty_array():
    source = []
    timsort(source)
    assert source == []


def test_one_element_array():
    source = [1]
    timsort(source)
    assert source == [1]


def test_sorted_array():
    source = [1, 2, 3]
    timsort(source)
    assert source == [1, 2, 3]


def test_negative_numbers():
    source = [5, 1, 3, -2, 11, 3]
    timsort(source)
    assert source == [-2, 1, 3, 3, 5, 11]

def test_1000_numbers():
    source = list(range(10_000, 0, -1))
    timsort(source)
    assert source == list(range(1, 10_001))
