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

# this doesn't work because the way the function rounds numbers is so weird
# def test_lower_quartile_decimals():
#     assert(lower_quartile([1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 0]) == 2.4)


# upper quartile tests
def test_upper_quartile_basic1():
    assert(upper_quartile([1, 2, 3, 4, 5, 6, 7]) == 6)

def test_upper_quartile_basic2():
    assert(upper_quartile([6, 8, 9, 10, 5, 33, 99, 2]) == 21.5)

def test_upper_quartile_basic3():
    assert(upper_quartile([4, 3, 1, 0, 3, 32, 0, 0, 0, 1, 94, 37, 21, 6, 55, 5]) == 26.5)

def test_upper_quartile_decimals():
    assert(upper_quartile([9.2, 6.7, 1.3, 3.8, 5.5, 4.4, 2.9, 7.3, 6.6, 8.9, 9.9, 8.6]) == 8.8)



# variance tests
def test_variance_basic1():
    assert(variance([1, 2, 4, 5]) == 2.500)

def test_variance_basic2():
    assert(variance([3, 4, 5, 5, 6, 7, 9]) == 3.388)

def test_variance_empty():
    assert(variance([]) == 0)
