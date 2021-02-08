import random

# AUXILIARIES FUNCTIONS


def isEven(num):
    if num % 2 == 0:
        return True


# STRATEGIES FUNCTIONS

# Strategy 5
def commonNumbersPick(numPicked):
    commonNumbers = [1, 11, 27, 28, 32]
    oneChoiceNumberCommon = random.choice(commonNumbers)
    return numPicked.append(oneChoiceNumberCommon)


# Strategy 3
def numberGroup(randomNum0123, randomNum):
    if randomNum0123 == 0 and 9 < randomNum and randomNum <= 36:
        return True
    elif randomNum0123 == 1 and ((1 <= randomNum and randomNum < 10) or (19 < randomNum and randomNum <= 36)):
        return True
    elif randomNum0123 == 2 and ((1 <= randomNum and randomNum < 20) or (29 < randomNum and randomNum <= 36)):
        return True
    elif randomNum0123 == 3 and 1 <= randomNum and randomNum < 30:
        return True


# Strategy 1 and 2
def oddEven(numPicked, randomNum0123):

    quantityEven = 0
    quantityOdd = 0

    quantityNumberLessEqual18 = 0
    quantityNumberGreaterEqual19 = 0

    result = []
    sumNumPicked = 0

    while len(numPicked) != 5:
        randomNum = random.randint(1, 36)

        if isEven(randomNum) and quantityEven < 3 and randomNum not in numPicked:
            if randomNum <= 18 and quantityNumberLessEqual18 < 3:
                if numberGroup(randomNum0123, randomNum):
                    quantityEven += 1
                    quantityNumberLessEqual18 += 1
                    numPicked.append(randomNum)
                    sumNumPicked += randomNum

            elif randomNum >= 19 and quantityNumberGreaterEqual19 < 3:
                if numberGroup(randomNum0123, randomNum):
                    quantityEven += 1
                    quantityNumberGreaterEqual19 += 1
                    numPicked.append(randomNum)
                    sumNumPicked += randomNum

        elif not isEven(randomNum) and quantityOdd < 3 and randomNum not in numPicked:
            if randomNum <= 18 and quantityNumberLessEqual18 < 3:
                if numberGroup(randomNum0123, randomNum):
                    quantityOdd += 1
                    quantityNumberLessEqual18 += 1
                    numPicked.append(randomNum)
                    sumNumPicked += randomNum

            elif randomNum >= 19 and quantityNumberGreaterEqual19 < 3:
                if numberGroup(randomNum0123, randomNum):
                    quantityOdd += 1
                    quantityNumberGreaterEqual19 += 1
                    numPicked.append(randomNum)
                    sumNumPicked += randomNum

    # print(sumNumPicked)

    # Strategy 4
    if 69 <= sumNumPicked and sumNumPicked <= 116:
        numPicked.sort()
        print(numPicked)
    else:
        numPicked = []
        commonNumbersPick(numPicked)
        randomNum0123 = random.randint(0, 3)
        oddEven(numPicked, randomNum0123)


def pickFantasy5():

    numPicked = []
    randomNum0123 = random.randint(0, 3)

    # Strategy 5
    commonNumbersPick(numPicked)

    # Strategy 1 and 2
    oddEven(numPicked, randomNum0123)


def main():
    pickFantasy5()


if __name__ == "__main__":
    main()
