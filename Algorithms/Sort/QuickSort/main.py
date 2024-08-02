import random


def swap(arr: list, ind_a: int, ind_b: int) -> None:
    arr[ind_a], arr[ind_b] = arr[ind_b], arr[ind_a]


class QuickSorter:
    def __init__(self, arr: list) -> None:
        self._arr = arr

    @property
    def array(self) -> list:
        return self._arr

    def sort(self, left_bound = None, right_bound = None) -> None:
        if left_bound is None:
            left_bound = 0
        if right_bound is None:
            right_bound = len(self.array)

        if left_bound >= right_bound:
            return

        pivot_pos = self._rand_partition(left_bound, right_bound)
        self.sort(left_bound, pivot_pos)
        self.sort(pivot_pos+1, right_bound)

    def _rand_partition(self, left_bound: int, right_bound: int) -> int:
        rand_pos = random.randint(left_bound, right_bound-1)
        swap(self.array, rand_pos, left_bound)
        return self._partition(left_bound, right_bound)

    def _partition(self, left_bound: int, right_bound: int) -> int:
        pivot = self.array[left_bound]
        before_pivot_pos = left_bound + 1
        for after_pivot_pos in range(left_bound+1, right_bound):
            if self.array[after_pivot_pos] < pivot:
                swap(self.array, before_pivot_pos, after_pivot_pos)
                before_pivot_pos += 1
        last_pos_before_pivot = before_pivot_pos - 1
        swap(self.array, left_bound, last_pos_before_pivot)
        return last_pos_before_pivot


sorter = QuickSorter([])
sorter.sort()
assert sorter.array == []

sorter = QuickSorter([1])
sorter.sort()
assert sorter.array == [1]

sorter = QuickSorter([1, 2, 3])
sorter.sort()
assert sorter.array == [1, 2, 3]

sorter = QuickSorter([5, 1, 3, -2, 11, 3])
sorter.sort()
assert sorter.array == [-2, 1, 3, 3, 5, 11]

sorter = QuickSorter([10, 9, 8, 0, -1])
sorter.sort()
assert sorter.array == [-1, 0, 8, 9, 10]

print("Well done!")
