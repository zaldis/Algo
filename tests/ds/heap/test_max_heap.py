from zaldisalgo.ds import MaxHeap


def test_max_item_getter() -> None:
    heap = MaxHeap(initial_items=[1, 2, 3, 4, 5])

    assert heap.get_max_item() == 5


def test_item_insertion() -> None:
    heap = MaxHeap(initial_items=[])

    heap.add_item(1)
    heap.add_item(2)
    heap.add_item(3)
    heap.add_item(0)

    assert heap.get_max_item() == 3


def test_item_extraction() -> None:
    heap = MaxHeap(initial_items=[1, 3, 2, 4, 3, 2, 1, 10, 5])

    assert heap.extract_max_item() == 10
    assert heap.extract_max_item() == 5
    assert heap.extract_max_item() == 4
    assert heap.extract_max_item() == 3
    assert heap.extract_max_item() == 3
    assert heap.extract_max_item() == 2
    assert heap.extract_max_item() == 2
    assert heap.extract_max_item() == 1
    assert heap.extract_max_item() == 1
    assert heap.size == 0
