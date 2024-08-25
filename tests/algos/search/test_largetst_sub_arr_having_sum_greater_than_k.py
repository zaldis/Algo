from zaldisalgo.algos.search import LengthSearcherOfLargestSubarrayHavingSumGreaterThanProvided


def test_common_case():
    assert LengthSearcherOfLargestSubarrayHavingSumGreaterThanProvided(sum_threshold=5).search(
        array=[-2, 1, 6, -3]
    ) == 2  # {1, 6}


def test_positive_values():
    assert LengthSearcherOfLargestSubarrayHavingSumGreaterThanProvided(sum_threshold=0).search(
        array=[1, 1, 1, 1, 1],
    ) == 5  # {1, 1, 1, 1, 1}


def test_negative_values():
    assert LengthSearcherOfLargestSubarrayHavingSumGreaterThanProvided(sum_threshold=0).search(
        array=[-1, -1, -1],
    ) == 0  # { }


def test_empty_array():
    assert LengthSearcherOfLargestSubarrayHavingSumGreaterThanProvided(sum_threshold=10).search(
        array=[],
    ) == 0  # { }
