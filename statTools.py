import pytest
from functools import reduce

typeChecker = lambda anyList: anyList if type(anyList) is list else []


def mean(anyList):
    anyList = typeChecker(anyList)
    if anyList != []:
        return sum(anyList) / len(anyList)
    else:
        pass


def median(anyList):
    anyList = typeChecker(anyList)
    if anyList != []:
        anyList.sort()
        if len(anyList) % 2 != 0:
            return anyList[int(len(anyList) // 2)]
        else:
            return (
                anyList[int(len(anyList) // 2)] + anyList[int(len(anyList) // 2 - 1)]
            ) / 2
    else:
        pass


def mode(anyList):
    anyList = typeChecker(anyList)
    if anyList != []:
        most = lambda anyList: (max(list(map(anyList.count, anyList))))
        return list(set(filter(lambda x: anyList.count(x) == most(anyList), anyList)))
    else:
        pass
