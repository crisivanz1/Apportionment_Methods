from Methods import *


# Finds how much difference there is from a number and the number it rounds up to, takes in a list.
def differences(standQuotaList):
    x = 0
    roundUpNumList = []
    roundUpNum = 0
    roundUpDifference = 0
    while x < len(standQuotaList):
        roundUpNum = math.ceil(standQuotaList[x])
        roundUpDifference = roundUpNum - standQuotaList[x]
        roundUpNumList.append(roundUpDifference)
        x += 1
    return roundUpNumList


# Combines 2 lists and a number into one list to be added to one complete list, takes in 2 lists and an integer.
def listCombine(statesList, differencesList, minQuota):
    fullList = []
    statesPopDifflist = []
    x = 0
    while x < len(statesList):
        statesPopDifflist.append(statesList[x])
        statesPopDifflist.append(differencesList[x])
        statesPopDifflist.append(minQuota[x])
        fullList.append(statesPopDifflist.copy())
        statesPopDifflist.clear()
        x += 1
    return fullList


# The Hamilton Method of apportionment is done here, takes in multiple values.
def hamiltonMethod(fullList, minQuota, units):
    if sum(minQuota) < units:
        diffUnits = units - sum(minQuota)
        fullList.sort(key=lambda a: a[1])
        x = 0
        while x < diffUnits:
            fullList[x][2] += 1
            x += 1
    return fullList
