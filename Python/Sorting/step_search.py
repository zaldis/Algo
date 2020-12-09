"""
    Step search (modification of binary search)
"""

import random
import time


def step_search(arr: list, item: int) -> int:
    n = len(arr)
    item_ind = 0
    delta_step = n // 2
    
    while delta_step >= 1:
        while (item_ind + delta_step < n and arr[item_ind + delta_step] <= item):
            item_ind += delta_step
        delta_step //= 2

    if arr[item_ind] == item:
        return item_ind
    return -1


if __name__ == '__main__': 
    times = []
    for size in [10, 100, 500, 1000, 2500, 5000, 7500, 12000]:
        arr = []
        for _ in range(size):
            arr.append(random.randint(0, 99))
        arr.sort()
        item = random.choice(arr)

        start = time.process_time()
        result = step_search(arr, item)
        end = time.process_time()
        if item == arr[result]:
            print('PASSED')
        else:
            print('FAILED')
        times.append(f'{(end-start) * 1000_000:.02f}')
    
    print(times)