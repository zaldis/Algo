from typing import Sequence, TypeVar

from zaldisalgo.utils.array import swap

T = TypeVar('T')

def bubble_sort(items: Sequence[T]) -> None:
    """Bubble sort implementation
    
    Inplace sorting.
    """
    for sorted_cnt in range(len(items)):
        for pos in range(1, len(items)-sorted_cnt):
            if items[pos] < items[pos-1]:
                swap(items, pos, pos-1)


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
    bubble_sort(people)
    print(*people, sep='\n')

