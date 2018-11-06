import pytest
from statTools import *

# Central Tendency --------------


def test_mean():
    assert mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5
    assert mean([]) == None


def test_median():
    assert median([2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6  # ODD
    assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5  # EVEN
    assert median([]) == None


def tests_mode():
    assert mode([1, 2, 3, 4, 4]) == [4]
    assert mode([1, 2, 2, 3, 3]) == [2, 3]
    assert mode([1, 2, 3, 1, 2, 3]) == [1, 2, 3]
    assert mode([]) == None


# Spread


def test_range():
    pass


def test_lower_quartile():
    pass


def test_upper_quartile():
    pass


def test_variance():
    pass


def test_standard_deviation():
    pass
