# Author : John Patrick Pitts
# Date   : June 23, 2021
# File   : MyOwnFunctions.py


# creates a list of consecutive integers from minimum to maximum, inclusive
def consecutive_number_list(minimum, maximum):
    return [n for n in range(minimum, maximum + 1)]


# returns the sum of all values in the parameter list
def list_sum(sum_list):
    ret = 0
    for n in sum_list:
        ret += n
    return ret


# returns the product of all values in the parameter list
def list_product(prod_list):
    ret = 1
    for n in prod_list:
        ret *= n
    return ret


# prints every even integer in the parameter list
def print_evens(values):
    for n in values:
        if n % 2 == 0:
            print(n, end=",")


# gets the consecutive integer list
this_list = consecutive_number_list(1, 13)


# performs all the print functions
print("Sum of list: ", list_sum(this_list))
print("Product of list: ", list_product(this_list))
print_evens(this_list)
