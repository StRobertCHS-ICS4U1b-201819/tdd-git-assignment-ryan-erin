import pytest
from statTools import *

def test_lower_quartile_basic1():
    assert(lower_quartile([1, 2, 3, 4, 5]) == 2)
