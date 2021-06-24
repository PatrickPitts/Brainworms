# Author : John Patrick Pitts
# Date   : June 21, 2021
# File   : Rectangle.py

# Info printed to the user
info = "Calculate the perimeter and area of a rectangle"

print(info)

# Gets data about the rectangle from the user and saves them to local variables
width = eval(input("What is the width? "))
length = eval(input("What is the length? "))

print("-" * 10)
print("calculating...")
print("-" * 10)

# perimeter calculation
perimeter = 2 * (width + length)

# area calculation
area = width * length

# prints calculations and data to the user
print("The width of the rectangle is :", width)
print("The length of the rectangle : ", length)
print("The area of the rectangle is ", area)
print("The perimeter of the rectangle is ", perimeter)
