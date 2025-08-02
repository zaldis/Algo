from collections.abc import Sequence

from zaldisalgo import ds


def sort[T](items: Sequence[T]) -> Sequence[T]:
    heap: ds.Heap[T] = ds.MaxHeap.of(*items)
    sorted_items = [None] * len(items)

    ind = len(items) - 1
    while heap.size:
        item = heap.extract_head()
        sorted_items[ind] = item
        ind -= 1
    return sorted_items


if __name__ == '__main__':
    source_items = [-2, 3, -7, 2, 1]
    assert sort(source_items) == sorted(source_items)
    print("Heap sort works as expected!")
