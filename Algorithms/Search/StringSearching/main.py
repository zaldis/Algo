class PatternSearcher:
    def __init__(self, text: str) -> None:
        self._text = text
        self._biggest_common_boundaries = []
        self._separator = '#'  # Text and pattern must not contain this symbol

    def search(self, pattern: str) -> int:
        source = pattern + self._separator + self._text
        self._find_biggest_common_boundaries(source)

        included_pattern_cnt = 0
        for common_boundary in self._biggest_common_boundaries:
            included_pattern_cnt += (common_boundary == len(pattern))
        return included_pattern_cnt

    def _find_biggest_common_boundaries(self, source: str) -> None:
        self._biggest_common_boundaries = [0] * len(source)
        for pos in range(1, len(source)):
            prev_common_boundary_pos = self._biggest_common_boundaries[pos-1]
            while prev_common_boundary_pos > 0 and source[pos] != source[prev_common_boundary_pos]:
                prev_common_boundary_pos = self._biggest_common_boundaries[prev_common_boundary_pos-1]

            curr_common_boundary_size = prev_common_boundary_pos
            if source[pos] == source[prev_common_boundary_pos]:
                curr_common_boundary_size += 1
            self._biggest_common_boundaries[pos] = curr_common_boundary_size


searcher = PatternSearcher("aba")
assert searcher.search("aba") == 1

searcher = PatternSearcher("sadasda")
assert searcher.search("sda") == 1

searcher = PatternSearcher("abababa")
assert searcher.search("aba") == 3

searcher = PatternSearcher("aaaa")
assert searcher.search("b") == 0

print("Well done!")
