"""
    Merge sort

    Complexity:
        Time: n * log(n)
        Space: n * log(n)
"""

import random
import time


def merge_sorted_parts(arr_a: list, arr_b: list) -> list:
    """
        Merging two sorted arrays into sorted one

        Selecting one by one elements from each parts 
        and putting smallest element to the result
    """
    sorted_result = []
    index_a = index_b = 0
    while index_a < len(arr_a) or index_b < len(arr_b):
        item_a = item_b = None
        if index_a < len(arr_a):
            item_a = arr_a[index_a]
        if index_b < len(arr_b):
            item_b = arr_b[index_b]
        
        if item_a is not None and item_b is not None:
            if item_a < item_b:
                sorted_result.append(item_a)
                index_a += 1
            else:
                sorted_result.append(item_b)
                index_b += 1
        else:
            if item_a is not None:
                sorted_result.append(item_a)
                index_a += 1
            else:
                sorted_result.append(item_b)
                index_b += 1
    return sorted_result


def merge_sort(arr: list) -> list:
    if len(arr) == 1:
        return arr

    divide_index = int(len(arr) / 2)
    sorted_left = merge_sort(arr[:divide_index])
    sorted_right = merge_sort(arr[divide_index:])

    return merge_sorted_parts(sorted_left, sorted_right)


if __name__ == '__main__':
    times = []
    for size in [10, 100, 500, 1000, 2500, 5000, 7500, 12000]:
        arr = []
        for _ in range(size):
            arr.append(random.randint(0, 99))
        start = time.process_time()
        result = merge_sort(arr)
        end = time.process_time()
        if sorted(arr) == result:
            print('PASSED')
        else:
            print('FAILED')
        times.append(f'{(end-start) * 1000_000:.02f}')
    
    print(times)