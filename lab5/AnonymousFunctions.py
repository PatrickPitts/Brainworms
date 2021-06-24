# Author : John Patrick Pitts
# Date   : June 23, 2021
# File   : AnonymousFunctions.py


# adds two parameters together
addTwo = lambda a, b: a + b

# finds the average between 3 parameters
average = lambda a, b, c: (a + b + c) / 3

# raises the parameter to the power of three
powerThree = lambda a: a * a * a

# returns "Hello World"
info = lambda: "Hello World"

# removes all spaces and makes all characters in the parameter string lower case
lowerStr = lambda s: s.strip().lower()

# gets characters from index 1 to 4, exclusive, and makes them upper case
subUpperStr = lambda s: s.strip().upper()[1:4]

# returns half the parameter list
halfList = lambda l: l[:int(len(l)/2)]

# testing anonymous functions
print("Add two: ", addTwo(9, 9))

print("Average three: ", average(1, 2, 3))

print("Power of three: ", powerThree(5))

print("Info: ", info())

print("Lower case string: ", lowerStr(" CWU    "))

print("Upper sub string: ", subUpperStr(" ccWucentral"))

print("First half of the list: ", halfList([1, 2, 3, 4, 5, 6]))
