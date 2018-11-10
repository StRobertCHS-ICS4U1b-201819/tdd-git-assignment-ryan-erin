def sort(num_list):
    new_list = []
    new_list.append(num_list[0])
    location = 0

    for i in range(1, len(num_list)):
        # if number is less than the first value in list
        if num_list[i] < new_list[0]:
            new_list.insert(0, num_list[i])
        # else check if it is greater than any of the other values
        else:
            # compares number to all the higher values
            for j in range(len(new_list)):
                if num_list[i] >= new_list[j]:
                    location = j + 1
            new_list.insert(location, num_list[i])
    return new_list

def lower_quartile(num_list):
    num_list = sort(num_list)
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