"""
    BigInteger is a data structure that emulates long arithmetic
"""

class BigInteger:
    """
        maximum is 1e4000; 4 digits by block
        block = digit of big integer
    """

    BLOCKS_COUNT = 1000
    BLOCK_SIZE = 4
    BLOCK_BASE = 10 ** BLOCK_SIZE

    def __init__(self, number: str):
        self._digits = [0] * self.BLOCKS_COUNT
        self._used_size = 0

        for char in number:
            digit = int(char)
            # shift one digit:
            # [1234, 4532, 1] -> [1234, 4532, 10] -> [1234, 5320, 14] -> [2340, 5321, 14]
            for i in range(self._used_size, -1, -1):
                self._digits[i+1] = self._digits[i+1] + (self._digits[i] * 10) // self.BLOCK_BASE
                self._digits[i] = (self._digits[i] * 10) % self.BLOCK_BASE
            self._digits[0] += digit
            if self._digits[self._used_size + 1] != 0:
                self._used_size += 1

    @classmethod
    def create_from_number(cls, number: int):
        return cls(str(number))


if __name__ == '__main__':
    big_num = BigInteger('12143424123467182634612354757')
    print(big_num._digits)

    big_num = BigInteger.create_from_number(1267578512346)
    print(big_num._digits)
