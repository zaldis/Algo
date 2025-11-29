from typing import Sequence, TypeVar
from zaldisalgo.utils.array import swap

T = TypeVar("T")

def insertion_sort(items: Sequence[T], start: int = None, end: int = None) -> None:
    if start is None:
        start = 0
    if end is None:
        end = len(items)
    for first_unsorted_ind in range(start+1, end):
        unsorted_ind = first_unsorted_ind
        while unsorted_ind > 0 and items[unsorted_ind] < items[unsorted_ind-1]:
            swap(items, unsorted_ind, unsorted_ind-1)
            unsorted_ind -= 1

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
    insertion_sort(people)
    print(*people, sep='\n')
