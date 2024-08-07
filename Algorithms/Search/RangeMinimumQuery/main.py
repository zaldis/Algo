import math
from dataclasses import dataclass


@dataclass
class Node:
    segment_start: int
    segment_end: int
    value: int


class MinimumValueSegmentTree:
    ROOT_NODE_IND = 1

    def __init__(self, values: list[int]) -> None:
        self._values = values
        # log 1 = 0, so it should be an edge case here
        # also there is empty node under the index 0, and actual nodes are started from index 1
        node_cnt = 2 if len(values) == 1 else math.ceil(
            math.log(len(values), 2)
        ) * len(values)
        self._tree: list[Node | None] = [None] * node_cnt
        self._build()

    def _build(self, node_ind: int = ROOT_NODE_IND, _from: int = 0, to: int | None = None) -> None:
        if to is None:
            to = len(self._values) - 1

        if _from == to:
            self._tree[node_ind] = Node(
                segment_start=_from,
                segment_end=to,
                value=self._values[_from],
            )
        else:
            mid_pos = (_from + to) // 2
            self._build(2*node_ind, _from, mid_pos)
            self._build(2*node_ind+1, mid_pos+1, to)
            self._tree[node_ind] = Node(
                segment_start=_from,
                segment_end=to,
                value=min(self._tree[2*node_ind].value, self._tree[2*node_ind+1].value)
            )

    def get_minimum_value(self, _from: int, to: int) -> int:
        def get_minimum_from_segment_tree(node_ind: int) -> int:
            node = self._tree[node_ind]
            segment_start = node.segment_start
            segment_end = node.segment_end

            if segment_end < _from or segment_start > to:
                return int(1e9)
            if _from <= segment_start and segment_end <= to:
                return node.value

            left_min = get_minimum_from_segment_tree(2 * node_ind)
            right_min = get_minimum_from_segment_tree(2*node_ind + 1)
            return min(left_min, right_min)

        return get_minimum_from_segment_tree(self.ROOT_NODE_IND)

    def update_value(self, index: int, value: int) -> None:
        def update_segment_tree(node_ind: int) -> None:
            node = self._tree[node_ind]
            segment_start = node.segment_start
            segment_end = node.segment_end

            if segment_start == segment_end:
                self._values[index] = value
                node.value = value
            else:
                mid_pos = (segment_start + segment_end) // 2
                if segment_start <= index <= mid_pos:
                    update_segment_tree(2*node_ind)
                else:
                    update_segment_tree(2*node_ind + 1)
                node.value = min(self._tree[2*node_ind].value, self._tree[2*node_ind+1].value)

        update_segment_tree(self.ROOT_NODE_IND)


segment_tree = MinimumValueSegmentTree([1])
assert segment_tree.get_minimum_value(0, 0) == 1
segment_tree.update_value(0, 5)
assert segment_tree.get_minimum_value(0, 0) == 5

segment_tree = MinimumValueSegmentTree([1, 5, 2, 4, 3])
assert segment_tree.get_minimum_value(0, 4) == 1
segment_tree.update_value(2, 6)
assert segment_tree.get_minimum_value(2, 4) == 3

segment_tree = MinimumValueSegmentTree([1, -1, 5, 8, 3, 2, 0, 7])
assert segment_tree.get_minimum_value(0, 7) == -1
segment_tree.update_value(1, 10)
assert segment_tree.get_minimum_value(0, 7) == 0

segment_tree = MinimumValueSegmentTree([1, -1, 5, 8, 3, 2])
assert segment_tree.get_minimum_value(0, 5) == -1

print("Well done!")
