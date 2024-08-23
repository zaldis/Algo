from zaldisalgo.algos.search import binary_search


def test_binary_search_in_empty_array() -> None:
    assert binary_search([], 12) == -1


def test_binary_search_in_array_with_one_element() -> None:
    assert binary_search([10], 10) == 0


def test_binary_search() -> None:
    array = [1, 2, 3]
    assert binary_search(array, 1) == 0
    assert binary_search(array, 2) == 1
    assert binary_search(array, 3) == 2


def test_binary_search_in_array_with_equal_elements() -> None:
    assert binary_search([1, 2, 2, 2, 4], 2) in {1, 2, 3}


def test_binary_search_with_array_without_element() -> None:
    assert binary_search([1, 2, 4, 4, 5, 6], 3) == -1
