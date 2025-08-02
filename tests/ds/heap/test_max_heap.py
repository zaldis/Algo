from zaldisalgo.ds import MaxHeap, Heap


def test_max_item_getter() -> None:
    heap: Heap[int] = MaxHeap.of(1, 2, 3, 4, 5)

    assert heap.head == 5


def test_item_insertion() -> None:
    heap: Heap[int] = MaxHeap()

    heap.add_node(1)
    heap.add_node(2)
    heap.add_node(3)
    heap.add_node(0)

    assert heap.head == 3


def test_item_extraction() -> None:
    heap: Heap[int] = MaxHeap.of(1, 3, 2, 4, 3, 2, 1, 10, 5)

    assert heap.extract_head() == 10
    assert heap.extract_head() == 5
    assert heap.extract_head() == 4
    assert heap.extract_head() == 3
    assert heap.extract_head() == 3
    assert heap.extract_head() == 2
    assert heap.extract_head() == 2
    assert heap.extract_head() == 1
    assert heap.extract_head() == 1
    assert heap.size == 0
