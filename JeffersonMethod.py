from Methods import *


# The Jefferson Method of apportionment is done here, takes in multiple values.
def JeffersonMethod(standardDivisor, popList, reps):
    modQuotasList = []
    roundedDown = []
    modQuota = 0
    JeffQuotaFinal = 0
    modDivisor = standardDivisor
    while JeffQuotaFinal < reps:
        modQuotasList.clear()
        modDivisor = modDivisor-(standardDivisor * 0.05)
        x = 0
        while x < len(popList):
            modQuota = popList[x]/modDivisor
            modQuotasList.append(modQuota)
            roundedDown = roundDownValue(modQuotasList)
            JeffQuotaFinal = sum(roundedDown)
            x += 1
    return JeffQuotaFinal, roundedDown, modQuotasList, modDivisor
