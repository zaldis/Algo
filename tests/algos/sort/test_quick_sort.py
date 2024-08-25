from zaldisalgo.algos.sort import quick_sort


def test_empty_array():
    assert quick_sort([]) == []


def test_one_element_array():
    assert quick_sort([1]) == [1]


def test_sorted_array():
    assert quick_sort([1, 2, 3]) == [1, 2, 3]


def test_negative_numbers():
    assert quick_sort([5, 1, 3, -2, 11, 3]) == [-2, 1, 3, 3, 5, 11]
