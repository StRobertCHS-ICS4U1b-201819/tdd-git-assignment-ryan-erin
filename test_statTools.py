import pytest
from statTools import *

def test_lower_quartile_basic1():
    assert(lower_quartile([1, 2, 3, 4, 5, 6, 7]) == 2)

def test_lower_quartile_basic2():
    assert(lower_quartile([8, 9, 18, 19, 28, 29]) == 9)

def test_lower_quartile_decimals1():
    assert(lower_quartile([8, 9, 18, 19, 28, 29, 38, 39]) == 13.5)

def test_lower_quartile_decimals2():
    assert(lower_quartile([2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]) == 8)

def test_variance_basic1():
    assert(variance([1, 2, 4, 5]) == 2.500)

def test_variance_basic2():
    assert(variance([3, 4, 5, 5, 6, 7, 9]) == 3.388)

def test_variance_empty():
    assert(variance([]) == 0)
