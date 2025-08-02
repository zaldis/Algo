""" Binary Search Implementation

Python has core library which implements binary search:
https://docs.python.org/3/library/bisect.html
"""
from typing import Sequence

def binary_search[T](array: Sequence[T], search_item) -> int:
    """ Find the position of the element in the ordered sequence

    :param array:       source ordered sequence
    :param search_item: an element which should be found
    :return:            the position of found element or -1
    """
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


if __name__ == '__main__':
    items = [0, 1, 1, 2, 2, 2, 3]
    exist_pos = binary_search(items, 2)
    not_exist_pos = binary_search(items, 7)
    print(f"The position of 2 in {items} is {exist_pos}")
    print(f"The position of 7 in {items} is {not_exist_pos}")