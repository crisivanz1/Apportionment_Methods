from HamiltonMethod import *
from JeffersonMethod import *


populationList, totalPopulation, reps, statesList = takeValues()
x = 0
print("")
while x < len(populationList):
    print("The population of " + statesList[x] + " is " + str(round(populationList[x])))
    x += 1
print("")
print("The total population is " + str(totalPopulation))


sD = findStandardDivisor(totalPopulation, reps)
print("\n" + "[Standard Divisor]")
print("For every " + str(round(sD, 3)) + " people, 1 representative is needed.")


standardQuotas = findStandardQuotas(populationList, sD)
x = 0
print("\n" + "[Standard Quotas]")
while x < len(populationList):
    print(statesList[x] + " should have " + str(standardQuotas[x]) + " representatives.")
    x += 1
print(str(reps) + " representatives need to be assigned.")


typeofMethod = int(input("Type 1 for Hamilton Method, type 2 for Jefferson Method: "))
if typeofMethod == 1:
    difference = differences(standardQuotas)
    minQuota = roundDownValue(standardQuotas)

    x = 0
    print("\n" + "[Minimum Quotas]")
    while x < len(minQuota):
        print("The minimum amount of representatives " + statesList[x] + " should have is " + str(minQuota[x]))
        x += 1
    print("A minimum of " + str(sum(minQuota)) + " representatives have been assigned.")

    combinedList = listCombine(statesList, difference, minQuota)
    hami = hamiltonMethod(combinedList, minQuota, reps)
    fullList = sorted(hami)

    x = 0
    print("\n" + "[Hamilton Method]")
    print("Using the Hamilton Method, the following should happen: ")
    while x < len(fullList):
        print(statesList[x] + " should receive " + str(fullList[x][2]) + " representatives.")
        x += 1
if typeofMethod == 2:
    jeff, jeffMethodNums, modQuotas, modifiedDivisor = JeffersonMethod(sD, populationList, reps, )

    print("\n" + "[Modified Divisor]")
    print("For every " + str(modifiedDivisor) + " people, 1 representative is needed.")
    x = 0
    print("\n" + "[Jefferson Method]")
    print("Using the Jefferson Method, the following should happen: ")
    while x < len(jeffMethodNums):
        print(statesList[x] + " should receive " + str(jeffMethodNums[x]) + " representatives.")
        x += 1
    print(str(jeff) + " representatives have been assigned.")


