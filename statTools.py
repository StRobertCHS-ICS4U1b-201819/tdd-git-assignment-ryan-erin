import math

def sort(num_list):
   '''
   Sorts a list of integers and/or floats in increasing numerical order and returns it as a new list.

   :param arg1: A list of integers and/or floats.
   :return: A new list of numbers and/or integers in increasing numerical order.
   '''
   new_list = []
   new_list.append(num_list[0])
   location = 0

   for i in range(1, len(num_list)):
       # check if the number is less than the first value in the new list
       if num_list[i] < new_list[0]:
           new_list.insert(0, num_list[i])
       # else, check if it is greater than any of the other values in the new list
       else:
           # compares number to all the higher values
           for j in range(len(new_list)):
               if num_list[i] >= new_list[j]:
                   location = j + 1
           new_list.insert(location, num_list[i])
   return new_list


def lower_quartile(num_list):
   '''
   Returns the median of the lower half of a given number list. If the length of the list is odd,
   the smaller half will be considered the lower half.

   :param arg1: A list of integers and/or floats.
   :return: Float rounded to 1 decimal place which is the lower quartile.
   '''
   try:
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
   except IndexError:
       return "List index out of range"
   except TypeError:
       return "A numeric data type was not provided"
   except:
       return "An error in the program has occurred"


def upper_quartile(num_list):
   '''
   Returns the median of the upper half of a given number list. If the length of the list is odd,
   the smaller half will be considered the upper half.

   :param arg1: A list of integers and/or floats.
   :return: Float rounded to 1 decimal place which is the upper quartile.
   '''
   try:
       num_list = sort(num_list)
       first = 0
       last = len(num_list)
       mid = ((first + last) // 2)
       if len(num_list) % 2 == 0:
           num_list = num_list[mid:]
       else:
           # if length of list is odd, take the smaller upper half
           num_list = num_list[mid + 1:]
       mid = ((mid + first) // 2)
       # check to see if the new list has an even or odd amount of numbers
       if len(num_list) % 2 == 0:
           # if even, will calculate the mean of the two middle numbers
           return round((num_list[mid] + num_list[mid - 1]) / 2, 1)
       else:
           return num_list[mid]
   except IndexError:
       return "List index out of range"
   except TypeError:
       return "A numeric data type was not provided"
   except:
       return "An error in the program has occurred"


def variance(num_list):
   '''
   Subtracts the mean from each data point and calculates the mean of each squared
   difference in order to determine how far each number in the list is from the mean.

   :param arg1: A list of integers and/or floats.
   :return: Float rounded to 3 decimal places which is the variance.
   '''
   try:
       if len(num_list) == 1:
           raise ValueError
       acc = 0
       answer = 0
       # calculates the mean of the number list
       for i in range(len(num_list)):
           acc += num_list[i]
       acc = acc/len(num_list)
       # squares the difference of the mean subtracting from the list values
       for j in range(len(num_list)):
           answer += (num_list[j] - acc) ** 2
       # round variance to 3 decimal places
       return round(answer/len(num_list), 3)
   except ZeroDivisionError:
       return "Cannot divide by zero"
   except ValueError:
       return "Illegal list"
   except TypeError:
       return "A numeric data type was not provided"
   except:
       return "An error in the program has occurred"


def standard_deviation(num_list):
   '''
   Takes the square root of the variance of the number list which is calculated by subtracting the mean
   from each data point and square rooting the mean of each squared difference. This is done in order
   to quantify the amount of variation or dispersion of a set of data values

   :param arg1: A list of integers and/or floats.
   :return: Float rounded to 1 decimal places which is the standard deviation.
   '''
   try:
       if len(num_list) == 1:
           raise ValueError
       return round(math.sqrt(variance(num_list)), 1)
   except TypeError:
       return "A numeric data type was not provided"
   except ValueError:
       return "Illegal list"
   except:
       return"An error in the program has occurred"