import pytest
from statTools import *

# my own unnecessary sort function tests
def test_sort_reverse():
    assert(sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6])

def test_sort_random1():
    assert(sort([6, 5, 4, 1, 3, 2]) == [1, 2, 3, 4, 5, 6])

def test_sort_random2():
    assert(sort([7, 45, 4, 1, 8, 13, 9]) == [1, 4, 7, 8, 9, 13, 45])



# lower quartile tests
def test_lower_quartile_basic1():
    assert(lower_quartile([1, 2, 3, 4, 5, 6, 7]) == 2)

def test_lower_quartile_basic2():
    assert(lower_quartile([8, 9, 18, 19, 28, 29]) == 9)

def test_lower_quartile_even_length1():
    assert(lower_quartile([8, 9, 18, 19, 28, 29, 38, 39]) == 13.5)

def test_lower_quartile_even_length2():
    assert(lower_quartile([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]) == 8)

def test_lower_quartile_unsorted1():
    assert(lower_quartile([5, 2, 7, 9, 11, 54, 3]) == 3)

def test_lower_quartile_unsorted2():
    assert(lower_quartile([5, 2, 38, 7, 9, 11, 54, 3]) == 4)

def test_lower_quartile_decimals():
    assert(lower_quartile([1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 0]) == 2.3)

def test_lower_quartile_negatives():
    assert(lower_quartile([-33, -2, -909, -22, -1, -5, 12, 9, 3.6]) == -27.5)



# upper quartile tests
def test_upper_quartile_basic1():
    assert(upper_quartile([1, 2, 3, 4, 5, 6, 7]) == 6)

def test_upper_quartile_basic2():
    assert(upper_quartile([6, 8, 9, 10, 5, 33, 99, 2]) == 21.5)

def test_upper_quartile_basic3():
    assert(upper_quartile([4, 3, 1, 0, 3, 32, 0, 0, 0, 1, 94, 37, 21, 6, 55, 5]) == 26.5)

def test_upper_quartile_decimals1():
    assert(upper_quartile([9.2, 6.7, 1.3, 3.8, 5.5, 4.4, 2.9, 7.3, 6.6, 8.9, 9.9, 8.6]) == 8.8)

def test_upper_quartile_decimals2():
    assert(upper_quartile([6.7, 8, 3, 2, 1, 0, 99]) == 8)

def test_upper_quartile_negatives():
    assert(upper_quartile([-1, -43, 3, 7, 50, -3, 5, 5, 1, 99]) == 7)



# variance tests
def test_variance_basic1():
    assert(variance([1, 2, 4, 5]) == 2.500)

def test_variance_basic2():
    assert(variance([3, 4, 5, 5, 6, 7, 9]) == 3.388)

def test_variance_ZeroDivisionError():
    assert(variance([]) == "Cannot divide by zero")

def test_variance_ValueError1():
    assert(variance([9]) == "Illegal list")

def test_variance_ValueError2():
    assert(variance(["HELLLLLLOOO"]) == "Illegal list")

def test_variance_TypeError():
    assert(variance("HELLLLLLOOO") == "A string was given instead of a number list")



# standard deviation tests
def test_standard_deviation_basic1():
    assert(standard_deviation([2, 3, 4, 7, 9]) == 2.6)

def test_standard_deviation_basic2():
    assert(standard_deviation([10, 2, 38, 23, 38, 23, 21]) == 12.3)

def test_standard_deviation_basic3():
    assert(standard_deviation([3, 4, 5, 5, 6, 7, 9]) == 1.8)

def test_standard_deviation_decimals():
    assert(standard_deviation([3.3, 4.2, 5.5, 2.3, 22, 5.9, 6.1]) == 6.2)
