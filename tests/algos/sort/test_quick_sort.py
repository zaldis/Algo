from zaldisalgo.algos.sort import quick_sort


def test_empty_array():
    items = []
    quick_sort(items)
    assert items == []


def test_one_element_array():
    items = [1]
    quick_sort(items)
    assert items == [1]


def test_sorted_array():
    items = [1, 2, 3]
    quick_sort(items)
    assert items == [1, 2, 3]


def test_negative_numbers():
    items = [5, 1, 3, -2, 11, 3]
    quick_sort(items)
    assert items == [-2, 1, 3, 3, 5, 11]
