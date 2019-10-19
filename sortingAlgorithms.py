from pudb import set_trace;
import time
import random
from guppy import hpy


def insertionSort(aList):
    for i in range(1, len(aList)):
        while aList[i] < aList[i - 1]: #While current smaller than previous
            aList[i - 1], aList[i] = aList[i], aList[i - 1] #Swap values
            if i >= 2: #Check if previous values are also to be swapped
                i -= 1
    return aList

#   --> Recursive mergeSort, returns a list of sorted elements
#       Divide and Conquer paradigm
def mergeSort(aList):
    if len(aList) <= 1:
        return aList
    mid = int(len(aList) / 2)

    #Divide the lists
    leftList = mergeSort(aList[:mid])
    rightList = mergeSort(aList[mid:])
    i = 0

    #Magic happens here, compare the first element in left n right,
    #pop the value and assign it to the list
    while len(leftList) != 0 and len(rightList) != 0:
        if leftList[0] < rightList[0]:
            aList[i] = leftList.pop(0)
        else:
            aList[i] = rightList.pop(0)
        i += 1

    #Go back up the recurssions, return the sorted result
    return aList[:-len(leftList + rightList)] + leftList + rightList

def bubbleSort(aList):
    for passnum in range(len(aList)-1,0,-1):
        for i in range(passnum):
            if aList[i]>aList[i+1]:
                aList[i], aList[i + 1], = aList[i + 1], aList[i]
    return aList

#def bubbleSort(aList):
#    checkBit = 0
#    while checkBit != 1:
#        checkBit = 1
#        for i in range(1, len(aList)):
#            if aList[i] < aList[i - 1]:
#                checkBit = 0
#                aList[i], aList[i - 1] = aList[i - 1], aList[i]
#    return aList


sortMe = [4,6,3,2]
sortMe = [4,6,3,2,8,1,5]
sortMe = []
for i in range (1, 100001):
    sortMe.append(random.randint(1, 10000))    

def main():
    #set_trace()
    h = hpy()
    lastTime = time.time()
    #print(insertionSort(sortMe))
    #print(mergeSort(sortMe))
    print(bubbleSort(sortMe))
    print(time.time() - lastTime, "\n\n")
    print(h.heap())
main()
