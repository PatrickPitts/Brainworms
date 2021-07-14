# Author : John Patrick Pitts
# Date   : July 6, 2021
# File   : Lab 8, MyFunctions.py
from typing import List, Tuple


# Prints message,
# Returns product of all extra integer parameters
def multiplyTogether(message: str, *args: int) -> int:
    # prints the first string parameter
    print(message)
    ret = 1
    # iterates across all extra integer parameters, multiplying with ret
    for n in args:
        ret *= n
    return ret


# Prints message,
# Returns sum of all extra integer parameters
def addTogether(message: str, *args: float) -> float:
    # prints the first string parameter
    print(message)
    ret = 0
    # iterates across all extra float parameters, adding to ret
    for n in args:
        ret += n
    return ret


# Returns the arithmetic average of all float parameters
def calculateAverage(*args: float) -> float:
    total = 0
    # iterates across all extra float parameters, calculating their sum
    for n in args:
        total += n
    # divides the sum by the number of parameters, then returns that value
    return total / len(args)


# Returns the minimum value of all parameter floats, and the index of that value
def findMin(*args: float) -> Tuple[float, int]:
    minVal = args[0]
    minIndex = 0
    # iterates across all float parameters to find the minimum value
    for i in range(len(args)):
        # checks if the current value is less than the minimum up to this index
        if args[i] < minVal:
            # updates the stored minimum value and the index
            minVal = args[i]
            minIndex = i
    return minVal, minIndex


# Returns the two largest floats in the list of parameters
def findTwoLargest(*args: float) -> Tuple[float, float]:
    # initializes the max and second-to-max of the first two float parameters
    maxs = [max(args[0], args[1]), min(args[0], args[1])]

    # iterates across the remaining float parameters
    for i in range(2, len(args)):
        n = args[i]
        # if the current value is greater than both max values,
        # push the first max down the list, and replace the first max value with the current value
        if n > maxs[0]:
            maxs[1] = maxs[0]
            maxs[0] = n
        # if the current value is greater than the second-to-max value,
        # replace the second-to-max value with the current value
        elif n > maxs[1]:
            maxs[1] = n
    return maxs[0], maxs[1]


# Returns the largest float in the list of parameters, and that numbers frequency of occurrence.
def countLargest(*args: float) -> Tuple[float, int]:
    # initializes the max value and the count
    m = args[0]
    count = 1
    for n in args:
        # if the current value is greater than the max value,
        # updates the max value, and resets the count to 1
        if n > m:
            m = n
            count = 1
        # if the current value is the same as the max value,
        # update the count of that value
        elif n == m:
            count += 1
    return m, count
