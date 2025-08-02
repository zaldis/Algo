from typing import Sequence, Final

from zaldisalgo.utils.array import swap
from zaldisalgo.ds.heap.protocols import Heap
from zaldisalgo.ds.heap.errors import EmptyHeapError


class MaxHeap[T]:
    """Binary Max Heap"""

    """
    First node is stored under the 1st index of the array to follow the logic:
    * root -> 1 (index)
    * left child -> 2 * root -> 2 (index)
    * right child -> 2 * root + 1 -> 3 (index)
    """
    _HEAD_IND: Final[int] = 1

    def __init__(self, initial_items: Sequence[T] = None) -> None:
        self._heap = [None]
        if initial_items is not None:
            self._heap += list(initial_items)
        self._build_heap()

    def __str__(self) -> str:
        return f"<MaxHeap items={self._heap}>"

    @staticmethod
    def of(*nodes: T) -> 'MaxHeap[T]':
        return MaxHeap(nodes)

    @property
    def size(self) -> int:
        """
        :return: Amount of actual nodes in the Heap
        """
        return len(self._heap) - 1

    @property
    def head(self) -> T:
        if not self.size:
            raise EmptyHeapError
        return self._heap[self._HEAD_IND]

    def add_node(self, node: T) -> None:
        self._heap.append(node)
        self._sift_up(self.size)

    def extract_head(self) -> T:
        if not self.size:
            raise EmptyHeapError
        max_item = self.head
        last_node = self._node(self.size)
        self._set_node(self._HEAD_IND, last_node)
        self._heapify(self._HEAD_IND)
        self._remove_node(self.size)
        return max_item

    def _build_heap(self) -> None:
        for position in self._get_upside_parent_indices():
            self._heapify(position)

    def _heapify(self, curr_ind: int) -> None:
        left_ind, right_ind = self._get_children_ind(curr_ind)
        largest_ind = curr_ind
        if left_ind <= self.size and self._node(left_ind)> self._node(curr_ind):
            largest_ind = left_ind
        if right_ind <= self.size and self._node(right_ind) > self._node(largest_ind):
            largest_ind = right_ind

        if largest_ind != curr_ind:
            swap(self._heap, curr_ind, largest_ind)
            self._heapify(largest_ind)

    def _sift_up(self, ind: int) -> None:
        parent_ind = self._parent_ind(ind)
        if parent_ind > 0 and self._node(parent_ind) < self._node(ind):
            swap(self._heap, ind, parent_ind)
            self._sift_up(parent_ind)

    def _get_upside_parent_indices(self) -> list[int]:
        """Get parent indices from very bottom to the root"""
        return [parent_ind for parent_ind in range(len(self._heap) // 2, 0, -1)]

    def _node(self, ind: int) -> T:
        return self._heap[ind]

    def _set_node(self, ind: int, new_node: T):
        self._heap[ind] = new_node

    def _remove_node(self, ind: int):
        del self._heap[ind]

    @staticmethod
    def _parent_ind(ind: int) -> int:
        return ind // 2

    @staticmethod
    def _get_children_ind(parent_index: int) -> tuple[int, int]:
        return 2 * parent_index, 2 * parent_index + 1


if __name__ == '__main__':
    heap: Heap = MaxHeap.of(4, 3, -10, 7, 5)
    print("Created heap is: ", heap)
    print("The head is: ", heap.head)
