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
