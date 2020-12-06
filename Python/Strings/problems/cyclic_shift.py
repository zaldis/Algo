"""
    Input:
        text - str
        pattern - str

    Output:
        Count of substrings from `text` to which pattern can be represented by cyclic shift

    Contest:
        https://acmp.ru/index.asp?main=task&id_task=50
"""

from typing import List


def get_zfunc(text: str) -> List[int]:
    n = len(text)
    l = r = 0
    z = [0] * n

    for i in range(1, n):
        if i < r:
            z[i] = min(z[i-l], r-i+1)
        while i+z[i] < n and text[z[i]] == text[i+z[i]]:
            z[i] += 1
        if i+z[i]-1 > r:
            l = i
            r = i+z[i]-1
    return z


def is_cyclic(text: str, pattern: str) -> bool:
    """
        Check if pattern can be represented by cyclic shift to text
    """
    zfunc = get_zfunc(pattern + '~' + text + text)
    return len(pattern) in zfunc


def solve(text, pattern) -> int:
    cyclic_substrs = 0
    for i in range(len(text)-len(pattern)+1):
        start = i
        end = i + len(pattern)
        target_substr = text[start:end]
        if is_cyclic(target_substr, pattern):
            cyclic_substrs += 1
    return cyclic_substrs


text = input()
pattern = input()
print(solve(text, pattern))
