import pytest
from statTools import *


# ---------------   Central Tendency ---------------------


def test_typeChecker():
    assert typeChecker(12) == []  # int
    assert typeChecker(1.2) == []  # float
    #   assert typeChecker() == []    # unable with empty values ❌
    assert typeChecker(None) == []  # none
    assert typeChecker([]) == []  # empty list
    assert typeChecker([1, 2]) == [1, 2]  # list
    assert typeChecker([1, 10 ** 1000])  # over max value


def test_mean():
    assert mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5  # General Cases

    # Corner Cases & Unusual Cases:
    assert mean([]) == None
    assert mean([1]) == 1
    assert mean(12) == None
    assert mean(None) == None


#   assert mean([1,10**1000]) # Out of range ❌


def test_median():
    assert median([2, 3, 4, 5, 6, 7, 8, 9, 10]) == 6  # ODD
    assert median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5  # EVEN

    # Corner Cases & Unusual Cases:
    assert median([]) == None
    assert median("hello") == None
    assert median(lambda x: [x]) == None


def tests_mode():
    assert mode([1, 2, 3, 4, 4]) == [4]  #  1 atom
    assert mode([1, 2, 2, 3, 3]) == [2, 3]  # 2 atom
    assert mode([1, 2, 3.3, 1, 2, 3.3]) == [1, 2, 3.3]  # 3 atom

    # Corner Cases & Unusual Cases:
    assert mode([]) == None
    assert mode(1.5) == None
    assert mode(map(lambda x: [x], [1])) == None


# ----------------------- Spread -------------------------


def test_rng():
    assert rng([1, 2, 3, 4]) == 4 - 1
    assert rng([]) == None
    assert rng(12) == None


# lower quartile tests
def test_lower_quartile_basic1():
    assert lower_quartile([1, 2, 3, 4, 5, 6, 7]) == 2


def test_lower_quartile_basic2():
    assert lower_quartile([8, 9, 18, 19, 28, 29]) == 9


def test_lower_quartile_even_length1():
    assert lower_quartile([8, 9, 18, 19, 28, 29, 38, 39]) == 13.5


def test_lower_quartile_even_length2():
    assert lower_quartile([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]) == 8


def test_lower_quartile_unsorted1():
    assert lower_quartile([5, 2, 7, 9, 11, 54, 3]) == 3


def test_lower_quartile_unsorted2():
    assert lower_quartile([5, 2, 38, 7, 9, 11, 54, 3]) == 4


def test_lower_quartile_decimals():
    assert lower_quartile([1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 0]) == 2.3


def test_lower_quartile_negatives():
    assert lower_quartile([-33, -2, -909, -22, -1, -5, 12, 9, 3.6]) == -27.5


def test_lower_quartile_IndexError():
    assert lower_quartile([]) == "List index out of range"


def test_lower_quartile_TypeError():
    assert lower_quartile("holaworld") == "A numeric data type was not provided"


# upper quartile tests
def test_upper_quartile_basic1():
    assert upper_quartile([1, 2, 3, 4, 5, 6, 7]) == 6


def test_upper_quartile_basic2():
    assert upper_quartile([6, 8, 9, 10, 5, 33, 99, 2]) == 21.5


def test_upper_quartile_basic3():
    assert upper_quartile([4, 3, 1, 0, 3, 32, 0, 0, 0, 1, 94, 37, 21, 6, 55, 5]) == 26.5


def test_upper_quartile_decimals1():
    assert (
        upper_quartile([9.2, 6.7, 1.3, 3.8, 5.5, 4.4, 2.9, 7.3, 6.6, 8.9, 9.9, 8.6])
        == 8.8
    )


def test_upper_quartile_decimals2():
    assert upper_quartile([6.7, 8, 3, 2, 1, 0, 99]) == 8


def test_upper_quartile_negatives():
    assert upper_quartile([-1, -43, 3, 7, 50, -3, 5, 5, 1, 99]) == 7


def test_upper_quartile_IndexError():
    assert upper_quartile([]) == "List index out of range"


def test_upper_quartile_TypeError():
    assert upper_quartile("bonjour world") == "A numeric data type was not provided"


# variance tests
def test_variance_basic1():
    assert variance([1, 2, 4, 5]) == 2.500


def test_variance_basic2():
    assert variance([3, 4, 5, 5, 6, 7, 9]) == 3.388


def test_variance_decimals():
    assert variance([0, 1.1, 2.33333, 2.4, 3, 5.121212, 7.6, 738]) == 59079.252


def test_variance_negatives():
    assert variance([-32, -9, -3, -1, 2.7, 6.6, 23, 343]) == 13213.324


def test_variance_ZeroDivisionError():
    assert variance([]) == "Cannot divide by zero"


def test_variance_ValueError1():
    assert variance([9]) == "Illegal list"


def test_variance_ValueError2():
    assert variance(["HELLLLLLOOO"]) == "Illegal list"


def test_variance_TypeError():
    assert variance("HELLLLLLOOO") == "A numeric data type was not provided"


# standard deviation tests
def test_standard_deviation_basic1():
    assert standard_deviation([2, 3, 4, 7, 9]) == 2.6


def test_standard_deviation_basic2():
    assert standard_deviation([10, 2, 38, 23, 38, 23, 21]) == 12.3


def test_standard_deviation_basic3():
    assert standard_deviation([3, 4, 5, 5, 6, 7, 9]) == 1.8


def test_standard_deviation_decimals1():
    assert standard_deviation([3.3, 4.2, 5.5, 2.3, 22, 5.9, 6.1]) == 6.2


def test_standard_deviation_decimals2():
    assert (
        standard_deviation([10.8, 2.927, 38.0, 23.00032, 38.11, 23.2, 21.342342, 7])
        == 12.3
    )


def test_standard_deviation_negatives():
    assert standard_deviation([-5, -2, -95.4, -2121, -0.3, -57, 3, 12]) == 695.5


def test_standard_deviation_TypeError():
    assert standard_deviation("good nightio") == "A numeric data type was not provided"


def test_standard_deviation_ValueError():
    assert standard_deviation([1]) == "Illegal list"
