def lower_quartile(num_list):
    first = 0
    last = len(num_list)
    mid = (first + last) // 2
    num_list = num_list[:mid]
    mid = (first + mid) // 2
    # check to see if the new list has an even or odd amount of numbers
    if len(num_list) % 2 == 0:
        return round((num_list[mid] + num_list[mid - 1])/2, 1)
    else:
        return num_list[mid]

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