from collections import namedtuple


IndexedPrefixSum = namedtuple('IndexedPrefixFunc', ['prefix_sum', 'prefix_index'])


class LengthSearcherOfLargestSubarrayHavingSumGreaterThanProvided:
    def __init__(self, sum_threshold: int) -> None:
        self._threshold = sum_threshold
        self._prefix_sums: list[IndexedPrefixSum] = []
        self._min_index_per_prefix_sum = []

    def search(self, array: list[int]) -> int:
        if not len(array):
            return 0

        self._build_prefix_sum(array)
        self._build_min_index_per_prefix_sum()

        curr_sum = 0
        max_subarray_len = 0
        for index, item in enumerate(array):
            curr_sum += item
            if curr_sum > self._threshold:
                max_subarray_len = index + 1
            else:
                # If SUM [0 .. index] <= K
                # Then check if it's possible to find: SUM [start .. index] > K
                start_index = self._find_closest_index_with_prefix_sum_less_or_equal_to(
                    curr_sum - self._threshold - 1
                )
                if start_index != -1 and self._min_index_per_prefix_sum[start_index] < index:
                    max_subarray_len = max(max_subarray_len, index - self._min_index_per_prefix_sum[start_index])
        return max_subarray_len

    def _find_closest_index_with_prefix_sum_less_or_equal_to(self, value: int) -> int:
        left_bound, right_bound = 0, len(self._prefix_sums) - 1
        result = -1

        while left_bound <= right_bound:
            mid = (left_bound + right_bound) // 2
            if self._prefix_sums[mid].prefix_sum <= value:
                result = mid
                left_bound = mid + 1
            else:
                right_bound = mid - 1
        return result

    def _build_prefix_sum(self, array: list[int]) -> None:
        """ Pre-calculate prefix sum for sub-arrays `[0..i]` for i in `[0..N]`

        The prefix sum structure is defined by: (prefix-sum, i)
        """
        for ind, item in enumerate(array):
            if ind > 0:
                self._prefix_sums.append(
                    IndexedPrefixSum(
                        prefix_sum=self._prefix_sums[ind - 1].prefix_sum + item,
                        prefix_index=ind,
                    )
                )
            else:
                self._prefix_sums.append(
                    IndexedPrefixSum(prefix_sum=item, prefix_index=ind)
                )
        self._prefix_sums.sort()

    def _build_min_index_per_prefix_sum(self) -> None:
        """ Pre-calculate minimum possible index to have the sum no more than prefix sum

        This pre-calculation will help to identify the start boundary of sub-array with expected minimum sum.
        """
        self._min_index_per_prefix_sum = [self._prefix_sums[0].prefix_index]
        for i, prefixSumForI in enumerate(self._prefix_sums[1:], start=1):
            self._min_index_per_prefix_sum.append(
                min(self._min_index_per_prefix_sum[i-1], prefixSumForI.prefix_index)
            )
