from .errors import EmptyHeapError


class MaxHeap:
    def __init__(self, initial_items: list[int]) -> None:
        self._heap = [None] + initial_items
        self._build_heap()

    @property
    def size(self) -> int:
        return len(self._heap) - 1

    def add_item(self, item: int) -> None:
        self._heap.append(item)
        self._sift_up(len(self._heap) - 1)

    def get_max_item(self) -> int:
        if not self.size:
            raise EmptyHeapError
        return self._heap[1]

    def extract_max_item(self) -> int:
        if not self.size:
            raise EmptyHeapError
        max_item = self._heap[1]
        self._heap[1] = self._heap[self.size]
        self._heapify(1)
        del self._heap[self.size]
        return max_item

    def _build_heap(self) -> None:
        for position in self._get_bottom_up_parent_positions():
            self._heapify(position)

    def _heapify(self, position: int) -> None:
        left_pos, right_pos = self._get_children_positions(position)
        largest_pos = position
        if left_pos < len(self._heap) and self._heap[left_pos] > self._heap[position]:
            largest_pos = left_pos
        if right_pos < len(self._heap) and self._heap[right_pos] > self._heap[largest_pos]:
            largest_pos = right_pos

        if largest_pos != position:
            self._heap[position], self._heap[largest_pos] = self._heap[largest_pos], self._heap[position]
            self._heapify(largest_pos)

    def _sift_up(self, position: int) -> None:
        parent_position = position // 2
        if parent_position > 0 and self._heap[parent_position] < self._heap[position]:
            self._heap[position], self._heap[parent_position] = self._heap[parent_position], self._heap[position]
            self._sift_up(parent_position)

    def _get_bottom_up_parent_positions(self) -> list[int]:
        return [i for i in range(len(self._heap) // 2, 0, -1)]

    @staticmethod
    def _get_children_positions(parent_position: int) -> tuple[int, int]:
        return 2 * parent_position, 2 * parent_position + 1


heap = MaxHeap(initial_items=[1, 2, 3, 4, 5])
assert heap.get_max_item() == 5

heap.add_item(1)
heap.add_item(2)
heap.add_item(3)
assert heap.get_max_item() == 5

heap.add_item(10)
assert heap.get_max_item() == 10

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

print("Well done!")
