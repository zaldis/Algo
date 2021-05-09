"""
    BigInteger is a data structure that emulates long arithmetic
"""

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
        self._blocks = [0] * self.BLOCKS_COUNT
        self._used_size = 0

        for char in number:
            digit = int(char)
            # shift one digit:
            # 145321234
            # [1234, 4532, 1] -> [1234, 4532, 10] -> [1234, 5320, 14] -> [2340, 5321, 14]
            for i in range(self._used_size, -1, -1):
                self._blocks[i+1] = self._blocks[i+1] + (self._blocks[i] * 10) // self.BLOCK_BASE
                self._blocks[i] = (self._blocks[i] * 10) % self.BLOCK_BASE
            self._blocks[0] += digit
            if self._blocks[self._used_size + 1] != 0:
                self._used_size += 1

    @classmethod
    def create(cls, number: Union[int, str]):
        if isinstance(number, int):
            number = str(number)
        return cls(number)

    def __str__(self):
        converted = list(
            map(
                lambda block: str(block).zfill(self.BLOCK_SIZE),
                reversed(self._blocks[:self._used_size+1])
            )
        )
        return ''.join(converted).lstrip('0')



if __name__ == '__main__':
    # Initialize from string representation
    big_num = BigInteger.create('12143424123467182634612354757')
    print(big_num._blocks)
    print(big_num)

    # Initialize from number
    big_num = BigInteger.create(1267578512346)
    print(big_num._blocks)
    print(big_num)
