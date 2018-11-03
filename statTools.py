import pytest
from functools import reduce

def mean(anyList):
    if anyList != []:
        return reduce(lambda a, b: a + b, anyList) / len(anyList)
    else:
        pass




