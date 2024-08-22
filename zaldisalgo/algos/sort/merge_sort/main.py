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


def merge_sort(array) -> list:
    sorter = MergeSorter(array)
    sorter.sort()
    return sorter.array
