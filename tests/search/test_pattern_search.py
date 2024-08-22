from zaldisalgo.algos.search import get_substring_count


def test_pattern_equals_to_source():
    source = pattern = "aba"
    assert get_substring_count(source, pattern) == 1


def test_pattern_inside_source():
    pattern = "aba"
    source = pattern + "xxx"
    assert get_substring_count(source, pattern) == 1


def test_pattern_overlapping_in_a_source():
    source = "abababa"
    pattern = "aba"
    assert get_substring_count(source, pattern) == 3


def test_pattern_is_not_in_source():
    pattern = "aba"
    source = "xxx"
    assert get_substring_count(source, pattern) == 0
