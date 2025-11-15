from zaldisalgo.algos.sort import bubble_sort

def test_empty_array():
    source = []
    bubble_sort(source)
    assert source == []


def test_one_element_array():
    source = [1]
    bubble_sort(source)
    assert source == [1]


def test_sorted_array():
    source = [1, 2, 3]
    bubble_sort(source)
    assert source == [1, 2, 3]


def test_negative_numbers():
    source = [5, 1, 3, -2, 11, 3]
    bubble_sort(source)
    assert source == [-2, 1, 3, 3, 5, 11]
