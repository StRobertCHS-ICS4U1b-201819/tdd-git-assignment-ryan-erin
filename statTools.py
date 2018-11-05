import pytest
from functools import reduce

def mean(anyList):
    if anyList != []:
        return reduce(lambda a, b: a + b, anyList) / len(anyList)
    else:
        pass

def median(anyList):
    if anyList != []:
        anyList.sort()
        if len(anyList) % 2 != 0:
            return anyList[int(len(anyList) // 2)]
        else:      
            return (anyList[int(len(anyList) // 2)] + anyList[int(len(anyList) // 2 - 1)]) /2
    else:
        pass
'''
def mode(anyList):
    if anyList != []:
        for i in range(len(anyList)):
        
        return i
    else:
        pass
        '''