from typing import Sequence, TypeVar

T = TypeVar('T')

def merge_sort(items: Sequence[T]) -> None:
    sorter = MergeSorter(items)
    sorter.sort()

class MergeSorter:
    def __init__(self, arr: Sequence[T]) -> None:
        self._arr = arr

    def sort(self, left_bound=None, right_bound=None) -> None:
        if left_bound is None:
            left_bound = 0
        if right_bound is None:
            right_bound = len(self._arr)

        if _is_range_with_one_element(left_bound, right_bound):
            return

        mid = (left_bound + right_bound) // 2
        self.sort(left_bound, mid)
        self.sort(mid, right_bound)
        merge(self._arr, left_bound, mid, right_bound)

def merge(items, start, mid, end) -> None:
    merged_items = []
    left_ind = start
    right_ind = mid
    while left_ind < mid and right_ind < end:
        if items[left_ind] <= items[right_ind]:
            merged_items.append(items[left_ind])
            left_ind += 1
        else:
            merged_items.append(items[right_ind])
            right_ind += 1
    while left_ind < mid:
        merged_items.append(items[left_ind])
        left_ind += 1
    while right_ind < end:
        merged_items.append(items[right_ind])
        right_ind += 1
    items[start:end] = merged_items


def _is_range_with_one_element(start: int, end: int) -> bool:
    return end - start <= 1


if __name__ == '__main__':
    from dataclasses import dataclass

    @dataclass
    class Person:
        name: str
        age: int

        def __le__(self, other):
            return self.age.__le__(other.age)

    people = [
        Person("Nikolai", 10),
        Person("Anton", 10),
        Person("Ivan", 25),
        Person("Alex", 10),
        Person("Anatolii", 15),
        Person("Alisa", 10)
    ]
    merge_sort(people)
    print(*people, sep='\n')
