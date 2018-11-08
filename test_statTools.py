import pytest
from statTools import *

def test_lower_quartile_basic1():
    assert(lower_quartile([1, 2, 3, 4, 5]) == 2)

def test_variance_basic1():
    assert(variance([1, 2, 4, 5]) == 2.500)

def test_variance_basic2():
    assert(variance([3, 4, 5, 5, 6, 7, 9]) == 3.388)

def test_variance_empty():
    assert(variance([]) == 0)
