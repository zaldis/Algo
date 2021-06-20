import random
from decimal import Decimal, getcontext

import pytest

from . import bigint
from .bigint import BigInteger, Sqrt

    
getcontext().prec = 10000


TEST_BAG_OF_BIG_NUMBERS = [
    12345,
    12834791273487123894789123748912738947,
    12389478923748237487123894789123748123749123748971238947,
    123947891263407862578061244712389470123741263476127346278189236496123487,
    9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
]


@pytest.mark.parametrize('n',TEST_BAG_OF_BIG_NUMBERS)
def test_sqrt(n):
    bn = BigInteger(n)

    res = Sqrt(bn).solve()
    expect = int(Decimal(n).sqrt())

    assert str(res) == str(expect), f'sqrt({n}) = {res}, {expect}'


@pytest.mark.parametrize('n', TEST_BAG_OF_BIG_NUMBERS)
def test_sum_from_1_to_n(n):
    bn = BigInteger(n)

    res = (
        bn * (bn + BigInteger(1)) // BigInteger(2)
    )
    expect = n * (n + 1) // 2

    assert str(res) == str(expect), f'Sum(1..{n}) = {res}, {expect}'


@pytest.mark.parametrize('a', TEST_BAG_OF_BIG_NUMBERS)
@pytest.mark.parametrize('b', TEST_BAG_OF_BIG_NUMBERS)
def test_division(a, b):
    big_a, big_b = (BigInteger(i) for i in [a, b])

    res = big_a // big_b
    expect = a // b

    assert str(res) == str(expect), f'{a} // {b} = {res}, {expect}'


@pytest.mark.parametrize('a', TEST_BAG_OF_BIG_NUMBERS)
@pytest.mark.parametrize('b', TEST_BAG_OF_BIG_NUMBERS)
def test_subtraction(a, b):
    if a < b:
        a, b = b, a
    big_a, big_b = (BigInteger(i) for i in [a, b])

    res = big_a - big_b
    expect = a - b

    assert str(res) == str(expect), f'{a} - {b} = {res}, {expect}'


@pytest.mark.parametrize('a', TEST_BAG_OF_BIG_NUMBERS)
@pytest.mark.parametrize('b', TEST_BAG_OF_BIG_NUMBERS)
def test_multiplication(a, b):
    big_a, big_b = (BigInteger(i) for i in [a, b])

    res = big_a * big_b
    expect = a * b

    assert str(res) == str(expect), f'{a} * {b} = {res}, {expect}'


@pytest.mark.parametrize('a', TEST_BAG_OF_BIG_NUMBERS)
@pytest.mark.parametrize('b', TEST_BAG_OF_BIG_NUMBERS)
def test_sum(a, b):
    big_a, big_b = (BigInteger(i) for i in [a, b])

    res = big_a + big_b
    expect = a + b

    assert str(res) == str(expect), f'{a} + {b} = {res}, {expect}'


@pytest.mark.parametrize('a', TEST_BAG_OF_BIG_NUMBERS)
@pytest.mark.parametrize('b', TEST_BAG_OF_BIG_NUMBERS)
def test_comparison(a, b):
    big_a, big_b = (BigInteger(i) for i in [a, b])

    assert (big_a == big_b) == (a == b)
    assert (big_a > big_b) == (a > b)
    assert (big_a >= big_b) == (a >= b)
    assert (big_a < big_b) == (a < b)
    assert (big_a <= big_b) == (a <= b)