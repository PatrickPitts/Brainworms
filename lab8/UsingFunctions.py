# Author : John Patrick Pitts
# Date   : July 6, 2021
# File   : Lab 8, UsingFunctions.py
import MyFunctions as mf


def main():
    print("-" * 10)
    print("Calling multiplyTogether(\"Hello!\", 2, 2, 2):")
    print("Printed message: ", end='')
    ans = mf.multiplyTogether("Hello!", 2, 2, 2)
    print("Result: %d" % ans)

    print("-" * 10)
    print("Calling addTogether(\"Hi!\", 5, 2, 3:)")
    print("Printed message: ", end='')
    ans = mf.addTogether("Hi!", 5, 2, 3)
    print("Result: %d" % ans)

    print("-" * 10)
    print("Calling calculateAverage(2, 1, 3):")
    print("Average: %d" % mf.calculateAverage(2, 1, 3))

    print("-" * 10)
    print("Calling findMin(10, 5, -4, 2, 7, 8):")
    print("Minimum: %d, at index %d" % mf.findMin(10, 5, -4, 2, 7, 8))

    print("-" * 10)
    print("Calling findTwoLargest(-2, 30, -4, 9, 1, 6):")
    print("Two Largest Numbers: %d, %d" % tuple(mf.findTwoLargest(-2, 30, -4, 9, 1, 6)))

    print("-" * 10)
    print("Calling countLargest(2, 2, 899, 56, -9, 87, 899, 764, -100, 899, 2, 2):")
    print("Largest Number: %d\nCount: %d" % tuple(mf.countLargest(2, 2, 899, 56, -9, 87, 899, 764, -100, 899, 2, 2)))


if __name__ == "__main__":
    main()
