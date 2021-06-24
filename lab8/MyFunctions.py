def multiplyTogether(message, *args):
    print(message)
    ret = 1
    for n in args:
        ret *= n
    return ret


def addTogether(message, *args):
    print(message)
    ret = 0
    for n in args:
        ret += n
    return ret


def calculateAverage(*args):
    total = 0
    for n in args:
        total += n
    return total / len(args)


def findMin(*args):
    minVal = args[0]
    minIndex = 0
    for i in range(len(args)):
        if args[i] < minVal:
            minVal = args[i]
            minIndex = i
    return minVal, minIndex


def findTwoLargest(*args):
    maxs = [max(args[0], args[1]), min(args[0], args[1])]
    for i in range(2, len(args)):
        n = args[i]
        if n > maxs[0]:
            maxs[1] = maxs[0]
            maxs[0] = n
        elif n > maxs[1]:
            maxs[1] = n
    return maxs


def countLargest(*args):
    m = args[0]
    count = 1
    for n in args:
        if n > m:
            m = n
            count = 1
        elif n == m:
            count += 1
    return m, count
