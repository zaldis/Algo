"""
    BigInteger is a data structure that emulates long arithmetic
"""

from array import array
from typing import Union


class BigInteger:
    """
        maximum is 1e4000; 4 digits by block
        block = digit of big integer
    """

    BLOCKS_COUNT = 1000
    BLOCK_SIZE = 4
    BLOCK_BASE = 10 ** BLOCK_SIZE

    def __init__(self, number: str):
        self._blocks = array('H', [0] * self.BLOCKS_COUNT)
        self._filled_blocks = 0

        for char in number:
            digit = int(char)
            # shift one digit:
            # 145321234
            # [1234, 4532, 1] -> [1234, 4532, 10] -> [1234, 5320, 14] -> [2340, 5321, 14]
            for i in range(self._filled_blocks, -1, -1):
                self._blocks[i+1] = self._blocks[i+1] + (self._blocks[i] * 10) // self.BLOCK_BASE
                self._blocks[i] = (self._blocks[i] * 10) % self.BLOCK_BASE
            self._blocks[0] += digit
            if self._blocks[self._filled_blocks + 1] != 0:
                self._filled_blocks += 1

    @classmethod
    def create(cls, number: Union[int, str] = '0'):
        if isinstance(number, int):
            number = str(number)
        return cls(number)

    def __add__(self, other: 'BigInteger') -> 'BigInteger':
        result_size = max(self._filled_blocks, other._filled_blocks)
        result = BigInteger.create()
        for i in range(result_size + 1):
            block_a = self._blocks[i]
            block_b = other._blocks[i]
            result._blocks[i+1] = (
                result._blocks[i] + block_a + block_b
            ) // self.BLOCK_BASE
            result._blocks[i] = (
                result._blocks[i] + block_a + block_b
            ) % self.BLOCK_BASE
        if result._blocks[result_size+1] > 0:
            result_size += 1
        result._filled_blocks = result_size
        return result

    def __eq__(self, big_num: 'BigInteger') -> bool:
        eq = False
        if self._filled_blocks == big_num._filled_blocks:
            eq = True
            for block_a, block_b in zip(self._blocks, big_num._blocks):
                eq &= block_a == block_b
        return eq

    def __gt__(self, big_num: 'BigInteger') -> bool:
        greater = False
        if self._filled_blocks > big_num._filled_blocks:
            greater = True
        elif self._filled_blocks == big_num._filled_blocks:
            i = self._filled_blocks
            while i > 0 and self._blocks[i] == big_num._blocks[i]:
                i -= 1
            greater = self._blocks[i] > big_num._blocks[i] 
        return greater

    def __ge__(self, big_num: 'BigInteger') -> bool:
        return self == big_num or self > big_num

    def __repr__(self):
        return f'{self.__class__}("{str(self)}")'

    def __str__(self):
        converted = list(
            map(
                lambda block: str(block).zfill(self.BLOCK_SIZE),
                reversed(self._blocks[:self._filled_blocks+1])
            )
        )
        return ''.join(converted).lstrip('0') or '0'



if __name__ == '__main__':
    big_num = BigInteger.create('0')
    print(big_num)
    print('========================================')

    # Initialize from string representation
    big_num = BigInteger.create('12143424123467182634612354757')
    print(big_num._blocks)
    print(big_num)
    print('========================================')

    # Initialize from number
    big_num = BigInteger.create(1267578512346)
    print(big_num._blocks)
    print(big_num)
    print('========================================')

    # Sum of two numbers
    a = BigInteger.create('7123687')
    b = BigInteger.create('8293843')
    assert str(a + b) == '15417530', 'Sum operation is failed'
    print(f'{a} + {b} = {a + b}')
    print('========================================')

    # Comparison of two numbers
    a = BigInteger.create('123456')
    b = BigInteger.create('123456')
    assert a == b
    assert a >= b
    assert a <= b
    print(f'{a} == {b}')

    a = BigInteger.create('1231238479')
    b = BigInteger.create('1231487279')
    assert not a >= b
    assert b > a
    assert a < b
    assert a <= b
    print(f'{b} > {a}')
    print('========================================')
