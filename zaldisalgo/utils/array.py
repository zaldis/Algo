from typing import Sequence


def swap(arr: Sequence, ind_a: int, ind_b: int) -> None:
    arr[ind_a], arr[ind_b] = arr[ind_b], arr[ind_a]
