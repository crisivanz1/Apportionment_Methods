import math


# Takes data input from user
def takeValues():
    x = 1
    totalValue = 0
    valuesList = []
    statesList = []
    numOfData = int(input("How many states are there? "))
    while x <= numOfData:
        statesList.append("State " + str(x))
        x += 1
    x = 1
    units = int(input("How many representatives are there to assign? "))
    while x <= numOfData:
        answer = float(input("How many people live in State " + str(x) + "? "))
        valuesList.append(answer)
        totalValue += answer
        x += 1
    return valuesList, totalValue, units, statesList


# Finds the standard divisor, takes in a list and a number of units.
def findStandardDivisor(totalValue, units):
    standardQuota = totalValue/units
    return standardQuota


# Rounds up the value of each number in a list, takes in a list.
def roundUpValue(valuesList):
    roundedList = []
    for quota in valuesList:
        roundedValue = math.ceil(quota)
        roundedList.append(roundedValue)
    return roundedList


# Rounds down the value of each number in a list, takes in a list.
def roundDownValue(valuesList):
    roundedList = []
    for quota in valuesList:
        roundedValue = math.floor(quota)
        roundedList.append(roundedValue)
    return roundedList


# Finds the standard quota of every data value in a list, takes in a list and a number.
def findStandardQuotas(valuesList, standardQuota):
    standardQuotaList = []
    sD = 0
    x = 0
    while x < len(valuesList):
        sD = valuesList[x]/standardQuota
        standardQuotaList.append(sD)
        x += 1
    return standardQuotaList











