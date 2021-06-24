# Author : John Patrick Pitts
# Date   : June 23, 2021
# File   : AverageExamScoresCalculator.py

sum_elements = 0
average_scores = 0
scores = []

# Prompts users to input one or more exam scores.
# doesn't check if input is accidentally a string type
while True:
    user_input = eval(input("Enter an exam score or -1 to stop: "))
    if user_input == -1:
        break
    else:
        scores.append(user_input)

# prints the input scores, and calculates the sum of all scores
print("Exam scores: ")
for num in scores:
    sum_elements += num
    print(num, end=",")

# calculates the average of the exam scores
average_scores = sum_elements / len(scores)

# prints the average of the exam scores
print()
print("Average exam score: ", average_scores)
