"""
    BigInteger is a data structure that emulates long arithmetic
"""
import copy

from array import array
from typing import Tuple, Union


class BigInteger:
    """
        maximum is 1e4000; 4 digits by block
        block = digit of big integer
    """

    BLOCKS_COUNT = 1000
    BLOCK_SIZE = 4
    BLOCK_BASE = 10 ** BLOCK_SIZE

    def __init__(self, number: str):
        self._blocks = array('h', [0] * self.BLOCKS_COUNT)
        self._filled_blocks = 1

        for char in number:
            digit = int(char)
            # shift one digit:
            # 145321234
            # [1234, 4532, 1] -> [1234, 4532, 10] -> [1234, 5320, 14] -> [2340, 5321, 14]
            for i in range(self._filled_blocks, -1, -1):
                self._blocks[i+1] = self._blocks[i+1] + (self._blocks[i] * 10) // self.BLOCK_BASE
                self._blocks[i] = (self._blocks[i] * 10) % self.BLOCK_BASE
            self._blocks[0] += digit
            if self._blocks[self._filled_blocks] != 0:
                self._filled_blocks += 1

    @classmethod
    def create(cls, number: Union[int, str] = '0'):
        if isinstance(number, int):
            number = str(number)
        return cls(number)

    def __add__(self, other: 'BigInteger') -> 'BigInteger':
        result_size = max(self._filled_blocks, other._filled_blocks)
        result = BigInteger.create()
        for i in range(result_size):
            block_a = self._blocks[i]
            block_b = other._blocks[i]
            base_sum = result._blocks[i] + block_a + block_b

            result._blocks[i+1] = base_sum // self.BLOCK_BASE
            result._blocks[i] = base_sum % self.BLOCK_BASE
        if result._blocks[result_size] > 0:
            result_size += 1
        result._filled_blocks = result_size
        return result

    def __sub__(self, b: 'BigInteger') -> 'BigInteger':
        result = copy.deepcopy(self)
        result -= b
        return result

    def __isub__(self, b: 'BigInteger') -> 'BigInteger':
        self.__inline_subtraction(b)
        return self

    def __sub(self, b: 'BigInteger', shift=0) -> 'BigInteger':
        result = copy.deepcopy(self)
        result.__inline_subtraction(b, shift)
        return result

    def __inline_subtraction(self, b: 'BigInteger', shift=0) -> None:
        if self.__is_less(b, shift):
            raise ValueError(f'Left operand should be greater than right. {self} - {b}')

        for i in range(b._filled_blocks):
            self._blocks[i+shift] -= b._blocks[i]
            if self._blocks[i+shift] < 0:
                j = i
                while j < b._filled_blocks and self._blocks[j+shift] < 0:
                    self._blocks[j+shift] += self.BLOCK_BASE
                    self._blocks[j+shift+1] -= 1
                    j += 1
        self._refresh_filled_blocks()

    def __mul__(self, other: 'BigInteger') -> 'BigInteger':
        if other._filled_blocks == 1:
            return self._mult_by_block(other._blocks[0])
        return self._mult_by_num(other)

    def __floordiv__(self, b: 'BigInteger') -> 'BigInteger':
        rest = self
        shift = self._filled_blocks - b._filled_blocks
        if self.__is_less(b, shift):
            shift -= 1

        result = BigInteger.create()
        result._filled_blocks = shift + 1
        while shift >= 0:
            result._blocks[shift], rest = self.__find_factor(rest, b, shift)
            shift -= 1
        return result

    @staticmethod
    def __find_factor(a: 'BigInteger', b: 'BigInteger', shift: int) -> Tuple[int, 'BigInteger']:
        down = 0
        up = BigInteger.BLOCK_BASE

        while up - 1 > down:
            c = b * BigInteger.create((up + down) // 2)
            if a.__is_greater(c, shift):
                down = (down + up) // 2
            elif a.__is_equal(c, shift):
                up = (up + down) // 2
                down = up
            else:
                up = (down + up) // 2

        factor = BigInteger.create((up + down) // 2)
        c = factor * b
        if a > c and c != BigInteger.create(0):
            a = a.__sub(c, shift)
        return int(factor), a

    def _mult_by_block(self, block: int) -> 'BigInteger':
        result = BigInteger.create()

        for i in range(self._filled_blocks):
            block_i = self._blocks[i]
            base_mult = result._blocks[i] + block_i * block
            result._blocks[i+1] = base_mult // self.BLOCK_BASE
            result._blocks[i] = base_mult % self.BLOCK_BASE

        result._refresh_filled_blocks()
        result._sift_overflow_blocks()
        return result

    def _mult_by_num(self, num: 'BigInteger') -> 'BigInteger':
        result = BigInteger.create()

        for i in range(self._filled_blocks):
            for j in range(num._filled_blocks):
                base_mult = result._blocks[i+j] + self._blocks[i] * num._blocks[j]
                result._blocks[i+j+1] += base_mult // self.BLOCK_BASE
                result._blocks[i+j] = base_mult % self.BLOCK_BASE

        result._refresh_filled_blocks()
        result._sift_overflow_blocks()
        return result

    def _sift_overflow_blocks(self):
        i = self._filled_blocks - 1
        while self._blocks[i] >= self.BLOCK_BASE:
            self._blocks[i+1] = self._blocks[i] // self.BLOCK_BASE
            self._blocks[i] = self._blocks[i] % self.BLOCK_BASE
            i += 1
            self._filled_blocks += 1 

    def _refresh_filled_blocks(self):
        self._filled_blocks = 1
        for start in range(self.BLOCKS_COUNT):
            if self._blocks[start] != 0:
                self._filled_blocks = start + 1

    def __eq__(self, b: 'BigInteger') -> bool:
        return self.__is_equal(b)

    def __is_equal(self, b: 'BigInteger', shift:int=0) -> bool:
        eq = False
        if self._filled_blocks == b._filled_blocks + shift:
            eq = True
            for i in range(b._filled_blocks):
                eq &= (self._blocks[i+shift] == b._blocks[i])
        return eq

    def __gt__(self, big_num: 'BigInteger') -> bool:
        return self.__is_greater(big_num)

    def __is_greater(self, big_num: 'BigInteger', shift=0) -> bool:
        greater = False
        if self._filled_blocks > big_num._filled_blocks + shift:
            greater = True
        elif self._filled_blocks == big_num._filled_blocks + shift:
            i = big_num._filled_blocks
            while i > 0 and self._blocks[i+shift] == big_num._blocks[i]:
                i -= 1
            greater = self._blocks[i+shift] > big_num._blocks[i] 
        return greater

    def __ge__(self, big_num: 'BigInteger') -> bool:
        return self == big_num or self > big_num

    def __is_less(self, b: 'BigInteger', shift=0) -> bool:
        return not any([
            self.__is_equal(b, shift),
            self.__is_greater(b, shift)
        ])

    def __int__(self):
        return int(str(self))

    def __repr__(self):
        return f'{self.__class__}("{str(self)}")'

    def __str__(self):
        converted = list(
            map(
                lambda block: str(block).zfill(self.BLOCK_SIZE),
                reversed(self._blocks[:self._filled_blocks])
            )
        )
        return ''.join(converted).lstrip('0') or '0'



if __name__ == '__main__':
    import random

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

    # Multiplication by block
    for i in range(100):
        a = random.randint(0, 1000000)
        b = random.randint(0, 1000000)
        assert a * b == int(BigInteger.create(a) * BigInteger.create(b))
        print(f'{a} * {b} == {a * b}')
    print('========================================')

    # Subtraction
    for i in range(100):
        a = random.randint(0, 1000000)
        b = random.randint(0, a)
        assert a - b == int(BigInteger.create(a) - BigInteger.create(b))
        print(f'{a} - {b} == {a - b}')
    print('========================================')

    # Division
    for i in range(100):
        a = random.randint(0, 1000000)
        b = random.randint(1, 1000000)
        assert a // b == int(BigInteger.create(a) // BigInteger.create(b))
        print(f'{a} // {b} == {a // b}')
    print('========================================')

    # Sum from 1 .. N
    for n in range(10**10, 10**10+100):
        bn = BigInteger.create(n)
        a = (
            bn * (bn + BigInteger.create(1)) // BigInteger.create(2)
        )

        b = n * (n + 1) // 2
        assert int(a) == b
