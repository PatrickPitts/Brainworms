# Author : John Patrick Pitts
# Date   : June 21, 2021
# File   : SeasonsAndDays.py

# imports essential libraries
import sys

# gets data input from the user
day_num = eval(input("Enter a number between 1 and 7: "))
season = input("Enter a season: ")
day = ""
month = ""

# lists to check against for type of season
spring = ["spring", "Spring", "SPRING"]
summer = ["summer", "Summer", "SUMMER"]
fall = ["fall", "Fall", "FALL"]
winter = ["winter", "Winter", "WINTER"]

# assigns values to 'day' based on the value of 'day_num'
# exits the script early if input is bad
if day_num == 1:
    day = "Monday"
elif day_num == 2:
    day = "Tuesday"
elif day_num == 3:
    day = "Wednesday"
elif day_num == 4:
    day = "Thursday"
elif day_num == 5:
    day = "Friday"
elif day_num == 6:
    day = "Saturday"
elif day_num == 7:
    day = "Sunday"
else:
    sys.exit()

# Assigns a value to 'month' based on 'season' and 'day_num'
# exits the script if input is bad
if season in spring:
    month = "March"
elif season in winter:
    month = "December"
elif season in fall:
    month = "September"
elif season in summer:
    if day_num <= 3:
        month = "June"
    else:
        month = "July"
else:
    sys.exit()

# prints data to user
print("The day is {day}, which day number {day_num}.".format(day=day, day_num=day_num))
print("The month is {month} which is in the {season}".format(month=month, season=season))

# prints extra data to user based on 'season' and 'day_num'
if season in summer and day_num == 6:
    print("Go swimming!")
