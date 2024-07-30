""" Binary Search Implementation

Python has core library which implements binary search:
https://docs.python.org/3/library/bisect.html
"""


def binary_search(array: list, search_item) -> int:
    start, end = 0, len(array)-1
    mid = (start+end) // 2

    while start < end:
        if array[mid] == search_item:
            break

        if array[mid] < search_item:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start+end) // 2

    if len(array) and array[mid] == search_item:
        return mid
    return -1


assert binary_search([], 12) == -1
assert binary_search([10], 10) == 0

assert binary_search([1, 2, 3], 1) == 0
assert binary_search([1, 2, 3], 2) == 1
assert binary_search([1, 2, 3], 3) == 2

assert binary_search([1, 2, 2, 2, 4], 2) in {1, 2, 3}

assert binary_search([1, 2, 4, 4, 5, 6], 3) == -1

print("Well done!")
