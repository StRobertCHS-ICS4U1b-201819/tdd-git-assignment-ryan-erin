"""
------------------------------------------------------------------------------------------------------------------------
Name: statTools.py
Purpose:
    Collection of functions calculating the central tendencies and spread of a set of numerical data
    - mean, median, mode - range, upper quartile, lower quartile, variance, standard deviation
Author: Ryan Erin
Created: 2018/11/11
------------------------------------------------------------------------------------------------------------------------
"""

import pytest

typeChecker = lambda anyList: anyList if type(anyList) is list else []


def mean(anyList): 
    """
    Returns the average of the integers in the list

    :param data: list of integers
    :return: Float rounded up to four decimals the average value of the data. None if no data.
    """
    anyList = typeChecker(anyList) # change all type to empty list, also as below
    if anyList != []:
        return sum(anyList) / len(anyList)
    else: 
        pass


def median(anyList):
    """
    Returns the middle number of the list
    :param data: list of integers
    :return: the middle integer in the list. average of the 2 numbers if two middle integers. None if no data.
    """
    anyList = typeChecker(anyList)
    if anyList != []:
        anyList.sort() # sorted list here
        if len(anyList) % 2 != 0: # if is even
            return anyList[int(len(anyList) // 2)]
        else:
            return (
                anyList[int(len(anyList) // 2)] + anyList[int(len(anyList) // 2 - 1)]
            ) / 2
    else:
        pass


def mode(anyList):
    """
    Returns the number that appears the most in the list.
    :param data: list of integers
    :return: list of integer(s) with the most frequency in the list. None if no data.
    """
    anyList = typeChecker(anyList)
    if anyList != []:
        most = lambda anyList: (max(list(map(anyList.count, anyList)))) 
        # function to count mode by single number
        return list(set(filter(lambda x: anyList.count(x) == most(anyList), anyList)))
        # then apply to each atom, filter the most serval number in the list.
    else:
        pass

def rng(anyList):
    """
    returns the difference between the greatest value and the smallest value in the data
    :param data: list of integers
    :return: the difference between the biggest and smallest number in the list
    """
    anyList = typeChecker(anyList)
    if anyList != []:
        return max(anyList) - min(anyList)
    else:
        pass
