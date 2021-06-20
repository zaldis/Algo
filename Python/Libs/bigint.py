"""
    BigInteger is a data structure that emulates long arithmetic
"""
import copy
import functools
from typing import Callable, List, Tuple, Union


def num_to_str(num: Union[str, int]) -> str:
    if not isinstance(num, (str, int)):
        raise TypeError(
            f'Number should int or str. Got {type(num)}.'
        )
    return str(num)


class BigInteger:
    """
        maximum is 1e4000; 4 digits by block
        block = digit of big integer
    """

    BLOCKS_COUNT = 1000
    BLOCK_SIZE = 4
    BLOCK_BASE = 10 ** BLOCK_SIZE

    def __init__(self, number: Union[int, str] = '0'):
        valid_number = num_to_str(number)
        self.__blocks = [0] * self.BLOCKS_COUNT
        self.__filled_blocks = 1

        for char in valid_number:
            digit = int(char)
            # shift one digit:
            # 145321234
            # [1234, 4532, 1] -> [1234, 4532, 10] -> [1234, 5320, 14] -> [2340, 5321, 14]
            for i in range(self.filled_blocks, -1, -1):
                self[i+1] = self[i+1] + (self[i] * 10) // self.BLOCK_BASE
                self[i] = (self[i] * 10) % self.BLOCK_BASE
            self[0] += digit
            if self[self.filled_blocks] != 0:
                self.filled_blocks += 1

    @property
    def filled_blocks(self) -> int:
        return self.__filled_blocks

    @filled_blocks.setter
    def filled_blocks(self, value):
        self.__filled_blocks = value

    @property
    def blocks(self):
        return self.__blocks[:self.filled_blocks]

    def __getitem__(self, index: int) -> int:
        self._validate_index(index)
        return self.__blocks[index]

    def __setitem__(self, index: int, value: int):
        self._validate_index(index)
        self.__blocks[index] = value

    def append_small_digits(self, digits: List[int]):
        self.__blocks[:0] = digits
        self.filled_blocks += len(digits)

    def append_big_digits(self, digits: List[int]):
        start = self.filled_blocks
        self.filled_blocks = end = start + len(digits)
        self.__blocks[start:end] = digits

    def _validate_index(self, index):
        if not isinstance(index, int):
            raise TypeError(f'Index must have int type. Got type {type(index)}')

        if index < 0 or index > self.BLOCKS_COUNT:
            raise ValueError(
                f'Index must be [0 .. {self.BLOCKS_COUNT}]. '
                f'Got {index}'
            )

    def __add__(self, other: 'BigInteger') -> 'BigInteger':
        result_size = max(self.filled_blocks, other.filled_blocks)
        result = BigInteger()
        for i in range(result_size):
            base_sum = result[i] + self[i] + other[i]
            result[i+1] = base_sum // self.BLOCK_BASE
            result[i] = base_sum % self.BLOCK_BASE

        if result[result_size] > 0:
            result_size += 1
        result.filled_blocks = result_size
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
            raise ValueError(
                f'Left operand should be greater than right. {self} - {b}'
            )

        for i in range(b.filled_blocks):
            self[i+shift] -= b[i]
            if self[i+shift] < 0:
                j = i
                while j < b.filled_blocks and self[j+shift] < 0:
                    self[j+shift] += self.BLOCK_BASE
                    self[j+shift+1] -= 1
                    j += 1
        self._refresh_filled_blocks()

    def __mul__(self, other: 'BigInteger') -> 'BigInteger':
        if other.filled_blocks == 1:
            return self._mult_by_block(other[0])
        return self._mult_by_num(other)

    def __floordiv__(self, b: 'BigInteger') -> 'BigInteger':
        result = BigInteger()

        if self > b:
            rest = self
            shift = self.filled_blocks - b.filled_blocks
            if self.__is_less(b, shift):
                shift -= 1

            result.filled_blocks = shift + 1
            while shift >= 0:
                result[shift], rest = self.__find_factor(rest, b, shift)
                shift -= 1
        elif self == b:
            result = BigInteger(1)

        return result

    @staticmethod
    def __find_factor(a: 'BigInteger', b: 'BigInteger', shift: int) -> Tuple[int, 'BigInteger']:
        down = 0
        up = BigInteger.BLOCK_BASE

        while up - 1 > down:
            c = b * BigInteger((up + down) // 2)
            if a.__is_greater(c, shift):
                down = (down + up) // 2
            elif a.__is_equal(c, shift):
                up = (up + down) // 2
                down = up
            else:
                up = (down + up) // 2

        factor = BigInteger((up + down) // 2)
        c = factor * b
        if a > c and c != BigInteger(0):
            a = a.__sub(c, shift)
        return int(factor), a

    def _mult_by_block(self, block: int) -> 'BigInteger':
        result = BigInteger()

        for i in range(self.filled_blocks):
            base_mult = result[i] + self[i] * block
            result[i+1] = base_mult // self.BLOCK_BASE
            result[i] = base_mult % self.BLOCK_BASE

        result._refresh_filled_blocks()
        result._sift_overflow_blocks()
        return result

    def _mult_by_num(self, num: 'BigInteger') -> 'BigInteger':
        result = BigInteger()

        for i in range(self.filled_blocks):
            for j in range(num.filled_blocks):
                base_mult = result[i+j] + self[i] * num[j]
                result[i+j+1] += base_mult // self.BLOCK_BASE
                result[i+j] = base_mult % self.BLOCK_BASE

        result._refresh_filled_blocks()
        result._sift_overflow_blocks()
        return result

    def _sift_overflow_blocks(self):
        i = self.filled_blocks - 1
        while self[i] >= self.BLOCK_BASE:
            self[i+1] = self[i] // self.BLOCK_BASE
            self[i] = self[i] % self.BLOCK_BASE
            i += 1
            self.filled_blocks += 1 

    def _refresh_filled_blocks(self):
        self.filled_blocks = 1
        for start in range(self.BLOCKS_COUNT):
            if self[start] != 0:
                self.filled_blocks = start + 1

    def __eq__(self, b) -> bool:
        return self.__is_equal(b)

    def __is_equal(self, b: 'BigInteger', shift:int=0) -> bool:
        eq = False
        if self.filled_blocks == b.filled_blocks + shift:
            eq = True
            for i in range(b.filled_blocks):
                eq &= (self[i+shift] == b[i])
        return eq

    def __gt__(self, big_num: 'BigInteger') -> bool:
        return self.__is_greater(big_num)

    def __is_greater(self, big_num: 'BigInteger', shift=0) -> bool:
        greater = False
        if self.filled_blocks > big_num.filled_blocks + shift:
            greater = True
        elif self.filled_blocks == big_num.filled_blocks + shift:
            i = big_num.filled_blocks
            while i > 0 and self[i+shift] == big_num[i]:
                i -= 1
            greater = self[i+shift] > big_num[i] 
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

    def __hash__(self):
        return hash(tuple(self.blocks))

    def __repr__(self):
        return f'{self.__class__}("{str(self)}")'

    def __str__(self):
        converted = (
            str(block).zfill(self.BLOCK_SIZE) 
            for block in reversed(self.blocks)
        )
        return ''.join(converted).lstrip('0') or '0'


def find_factor(down: BigInteger, 
                up: BigInteger, 
                value: BigInteger, 
                func: Callable[[BigInteger], BigInteger]) -> BigInteger:
    while down + BigInteger(1) < up:
        target = (up + down) // BigInteger(2)
        target_value = func(target)
        if target_value < value:
            down = target
        elif target_value > value:
            up = target
        else:
            up = down = target
    return (up + down) // BigInteger(2)


class Sqrt:
    """
        Calculate square root from BigInteger structure
    """

    def __init__(self, a: BigInteger):
        self.target: BigInteger = a

    def solve(self):
        result = BigInteger()
        stages = self._get_sqrt_stages()
    
        stage = stages.pop()
        result, rest = self._get_initial_factor(stage)

        for stage in reversed(stages):
            factor, rest = self._get_factor(stage, rest, result)
            result.append_small_digits(factor.blocks)
        return result

    def _get_sqrt_stages(self):
        stage = BigInteger()
        stages = []
        for i, block in enumerate(self.target.blocks):
            if i % 2 == 0:
                stage = BigInteger(block)
            else:
                stage.append_big_digits([block])
                stages.append(stage)

        if i % 2 == 0:
            stages.append(stage)

        return stages

    def _get_initial_factor(self, stage: BigInteger):
        factor = find_factor(BigInteger(0), 
                             BigInteger(BigInteger.BLOCK_BASE), 
                             stage, lambda f: f*f)
        rest = stage - factor * factor
        return factor, rest

    def _get_factor(self, stage: BigInteger, rest: BigInteger, result: BigInteger):
        if int(rest) != 0:
            print(rest.blocks)
            stage.append_big_digits(rest.blocks)
            print(f'stage: {stage}')

        factor = find_factor(BigInteger(0),
                             BigInteger(BigInteger.BLOCK_BASE),
                             stage, 
                             lambda f: self._factor_value(f, result)
        )
        rest = stage - self._factor_value(factor, result)
        return factor, rest

    @staticmethod
    def _factor_value(factor: BigInteger, result: BigInteger) -> BigInteger:
        return (
            BigInteger(2) * result * BigInteger(factor.BLOCK_BASE) + factor
        ) * factor


if __name__ == '__main__':
    pass