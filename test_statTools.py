from statTools import *

# Central Tendency

def test_typeChecker():
    assert typeChecker(12) == [] # int
    assert typeChecker(1.2) == [] # float
#   assert typeChecker() == []    # unable with empty values ❌
    assert typeChecker(None) == [] # none
    assert typeChecker([]) == [] # empty list
    assert typeChecker([1,2]) == [1,2] # list
    assert typeChecker([1,10**1000]) # over max value

def test_mean():
    assert mean([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5.5 # General Cases   

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
    assert mode([1, 2, 3, 4, 4]) == [4] #  1 atom
    assert mode([1, 2, 2, 3, 3]) == [2, 3] # 2 atom
    assert mode([1, 2, 3, 1, 2, 3]) == [1, 2, 3] # 3 atom

# Corner Cases & Unusual Cases:
    assert mode([]) == None
    assert mode(1.5) == None
    assert mode(map(lambda x: [x],[1])) == None


# Spread


def test_range():
    pass

