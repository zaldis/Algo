"""
    Counting sort

    Complexity:
        Time: O(n)
        Space: O(max), max - largest value in the input array
"""

import random
import time


MAX_VALUE = 100


def counting_sort(arr: list) -> list:
    counter = [0] * MAX_VALUE

    for item in arr:
        counter[item] += 1

    result = []
    for element, cnt in enumerate(counter):
        for _ in range(cnt):
            result.append(element)
    return result


if __name__ == '__main__':
    times = []
    for size in [10, 100, 500, 1000, 2500, 5000, 7500, 12000]:
        arr = []
        for _ in range(size):
            arr.append(random.randint(0, MAX_VALUE-1))
        start = time.process_time()
        result = counting_sort(arr)
        end = time.process_time()
        if sorted(arr) == result:
            print('PASSED')
        else:
            print('FAILED')
        times.append(f'{(end-start) * 1000_000:.02f}')
    
    print(times)
