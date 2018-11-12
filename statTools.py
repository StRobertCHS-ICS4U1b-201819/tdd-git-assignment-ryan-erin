import math

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
        # if even, will calculate the mean of the two middle numbers
        return round((num_list[mid] + num_list[mid - 1]) / 2, 1)
    else:
        return num_list[mid]


def upper_quartile(num_list):
    num_list = sort(num_list)
    first = 0
    last = len(num_list)
    mid = ((first + last) // 2)
    if len(num_list) % 2 == 0:
        num_list = num_list[mid:]
    else:
        num_list = num_list[mid + 1:]
    mid = ((mid + first) // 2)
    # check to see if the new list has an even or odd amount of numbers
    if len(num_list) % 2 == 0:
        # if even, will calculate the mean of the two middle numbers
        return round((num_list[mid] + num_list[mid - 1]) / 2, 1)
    else:
        return num_list[mid]


def variance(num_list):
    try:
        if len(num_list) == 1:
            raise ValueError
        acc = 0
        answer = 0
        # calculates the mean of the number list
        for i in range(len(num_list)):
            acc += num_list[i]
        acc = acc/len(num_list)

        for j in range(len(num_list)):
            answer += (num_list[j] - acc) ** 2
        # round variance to 3 decimal places
        return round(answer/len(num_list), 3)
    # except TypeError:
    #     raise TypeError("A string was given instead of a number")
    # except ValueError:
    #     return "Illegal list"
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except ValueError:
        return "Illegal list"
    except TypeError:
        return "A string was given instead of a number list"


def standard_deviation(num_list):
    return round(math.sqrt(variance(num_list)), 1)