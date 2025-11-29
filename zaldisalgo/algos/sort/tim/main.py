from typing import Sequence, TypeVar
from dataclasses import dataclass

from zaldisalgo.algos.sort.insertion.main import insertion_sort
from zaldisalgo.algos.sort.merge.main import merge

T = TypeVar('T')

def timsort(items: Sequence[T]) -> None:
    TimSort(items).sort()

class TimSort:
    RUN_BLOCK_TARGET_SIZE = 32

    def __init__(self, items: Sequence[T]) -> None:
        self._items = items
        self._run_block_size = self._get_size_of_run_block()
        self._run_blocks = []
        self._start_of_run_block = 0

    @property
    def size(self) -> int:
        return len(self._items)

    def sort(self) -> None:
        while self._start_of_run_block < self.size:
            run_block = self._build_run_block()
            self._run_blocks.append(run_block)
            self._start_of_run_block = run_block.end
            while self._is_last_run_block_big_enough_to_merge():
                self._merge_last_two_run_blocks()
        while self._is_few_run_blocks():
            self._merge_last_two_run_blocks()

    def _build_run_block(self) -> 'Block':
        sorted_block = self._find_sorted_block()
        run_block = self._convert_to_run_block(sorted_block)
        return run_block

    def _convert_to_run_block(self, sorted_block: 'Block') -> 'Block':
        if len(sorted_block) < self._run_block_size:
            end = min(self._start_of_run_block + self._run_block_size, self.size)
            insertion_sort(self._items, start=self._start_of_run_block, end=end)
            sorted_block.end = end
        return sorted_block

    def _merge_last_two_run_blocks(self) -> None:
        block1 = self._run_blocks[-2]
        block2 = self._run_blocks[-1]
        merge(self._items, block1.start, block1.end, block2.end)
        self._run_blocks.pop()
        self._run_blocks[-1] = Block(block1.start, block2.end)

    def _find_sorted_block(self) -> 'Block':
        start = self._start_of_run_block
        end = start + 1
        if end == self.size:
            return Block(start, end)

        if self._items[end] < self._items[start]:
            end = self._find_descending_block_end(end)
            self._items[start:end] = reversed(self._items[start:end])
        else:
            end = self._find_ascending_block_end(end)
        return Block(start, end)

    def _find_ascending_block_end(self, start: int) -> int:
        end = start
        while end < self.size and self._items[end] >= self._items[end - 1]:
            end += 1
        return end

    def _find_descending_block_end(self, start: int) -> int:
        end = start
        while end < self.size and self._items[end] < self._items[end-1]:
            end += 1
        return end

    def _is_few_run_blocks(self) -> bool:
        return len(self._run_blocks) > 1

    def _is_last_run_block_big_enough_to_merge(self) -> bool:
        return self._is_few_run_blocks() and len(self._run_blocks[-2]) <= len(self._run_blocks[-1])

    def _get_size_of_run_block(self) -> int:
        """ The size of "Run" block for timsort algorithm

        It should be the power of two for efficiency of merge sort.
        """
        n = len(self._items)
        is_odd = 0
        while n >= TimSort.RUN_BLOCK_TARGET_SIZE:
            is_odd |= n & 1
            n >>= 1
        return n + is_odd

@dataclass
class Block:
    start: int
    end: int

    def __len__(self) -> int:
        return self.end - self.start


if __name__ == '__main__':
    @dataclass
    class Person:
        name: str
        age: int

        def __lt__(self, other):
            return self.age.__lt__(other.age)
        def __ge__(self, other):
            return self.age.__ge__(other.age)

    people = [
        Person("Nikolai", 10),
        Person("Anton", 10),
        Person("Ivan", 25),
        Person("Alex", 10),
        Person("Anatolii", 15),
        Person("Alisa", 10)
    ]
    timsort(people)
    print(*people, sep='\n')