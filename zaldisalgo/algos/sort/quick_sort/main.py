import random
from typing import Generic, Sequence, TypeVar

from zaldisalgo.utils.array import swap

T = TypeVar('T')


def quick_sort(items: Sequence[T]) -> None:
    _QuickSort(items).sort()


class _QuickSort(Generic[T]):
    def __init__(self, items: Sequence[T]) -> None:
        self._items = items

    def sort(self, start_index=None, end_index=None) -> None:
        start_index = 0 if start_index is None else start_index
        end_index = len(self._items) if end_index is None else end_index

        if _is_range_with_single_element(start_index, end_index):
            return

        pivot_pos = self._rand_partition(start_index, end_index)
        self.sort(start_index, pivot_pos)
        self.sort(pivot_pos + 1, end_index)

    def _rand_partition(self, start_index: int, end_index: int) -> int:
        self._put_pivot_item_on_top(start_index, end_index)
        return self._place_items_according_to_pivot(start_index, end_index)

    def _put_pivot_item_on_top(self, start_index: int, end_index: int):
        rand_pos = random.randint(start_index, end_index-1)
        pivot_pos = start_index
        swap(self._items, rand_pos, pivot_pos)

    def _place_items_according_to_pivot(self, start_index: int, end_index: int) -> int:
        curr_pivot_pos = start_index
        pivot = self._items[curr_pivot_pos]
        expected_pivot_pos = curr_pivot_pos
        for pos in range(curr_pivot_pos+1, end_index):
            if self._items[pos] < pivot:
                expected_pivot_pos += 1
                swap(self._items, expected_pivot_pos, pos)
        swap(self._items, curr_pivot_pos, expected_pivot_pos)
        return expected_pivot_pos


def _is_range_with_single_element(left_bound: int, right_bound: int) -> bool:
    return left_bound >= right_bound


if __name__ == '__main__':
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str
        age: int

        def __lt__(self, other):
            return self.age.__lt__(other.age)

    people = [
        Person("Nikolai", 10),
        Person("Anton", 10),
        Person("Ivan", 25),
        Person("Alex", 10),
        Person("Anatolii", 15),
        Person("Alisa", 10)
    ]
    quick_sort(people)
    print(*people, sep='\n')
