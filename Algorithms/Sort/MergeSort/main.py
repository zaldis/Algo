class MergeSorter:
    def __init__(self, arr: list) -> None:
        self._arr = arr

    def sort(self, left_bound=None, right_bound=None) -> None:
        if left_bound is None:
            left_bound = 0
        if right_bound is None:
            right_bound = len(self._arr)

        if right_bound - left_bound <= 1:
            return

        mid = (left_bound + right_bound) // 2
        self.sort(left_bound, mid)
        self.sort(mid, right_bound)
        self._merge(left_bound, mid, right_bound)

    def _merge(self, start, mid, end):
        sorted_total_arr = []
        left_ind = start
        right_ind = mid
        while left_ind < mid or right_ind < end:
            if left_ind >= mid:
                sorted_total_arr.append(self._arr[right_ind])
                right_ind += 1
            elif right_ind >= end:
                sorted_total_arr.append(self._arr[left_ind])
                left_ind += 1
            elif self._arr[left_ind] <= self._arr[right_ind]:
                sorted_total_arr.append(self._arr[left_ind])
                left_ind += 1
            else:
                sorted_total_arr.append(self._arr[right_ind])
                right_ind += 1
        self._arr[start:end] = sorted_total_arr

    @property
    def array(self) -> list:
        return self._arr


sorter = MergeSorter([])
sorter.sort()
assert sorter.array == []

sorter = MergeSorter([1])
sorter.sort()
assert sorter.array == [1]

sorter = MergeSorter([1, 2, 3])
sorter.sort()
assert sorter.array == [1, 2, 3]

sorter = MergeSorter([5, 1, 3, -2, 11, 3])
sorter.sort()
assert sorter.array == [-2, 1, 3, 3, 5, 11]

sorter = MergeSorter([10, 9, 8, 0, -1])
sorter.sort()
assert sorter.array == [-1, 0, 8, 9, 10]

print("Well done!")
