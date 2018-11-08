def lower_quartile(intList):
    first = 0
    last = len(intList)
    mid = (first+last) // 2
    last = mid
    mid = (first + last) // 2
    midItem = intList[mid]
    return midItem

def upper_quartile():
    pass

def variance(intList):
    if len(intList) <= 1:
        return 0
    acc = 0
    variance = 0
    for i in range(len(intList)):
        acc += intList[i]
    acc = acc/len(intList)

    for j in range(len(intList)):
        variance += (intList[j] - acc) ** 2
    # round variance to 3 decimal places
    return round(variance/len(intList), 3)

def standard_deviation():
    pass