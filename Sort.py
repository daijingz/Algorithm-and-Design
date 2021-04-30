# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# This file includes programs with 4 different kinds of sorting algorithm
# All of those target inputs are lists consist of unrepeated integers and floats
# Sort output is ascending-integer list
import random


def checkAvailable(inputList):
    i = 0
    while i < len(inputList):
        if isinstance(inputList[i], (float, int)):
            return False
        i += 1

    for j in inputList:
        if inputList.count(j) > 1:
            return False

    return True


def SelectionSort(inputList):
    if not checkAvailable(inputList):
        raise ValueError

    output = []
    loopList = inputList
    while len(loopList) > 0:
        output += [min(loopList)]
        loopList.remove(min(loopList))
    return output


def InsertionSort(inputList):
    if not checkAvailable(inputList):
        raise ValueError

    output = []
    for i in inputList:
        output = Insertion(output, i)
        print(output)
    return output


# Helper function of Insertion Sort
def Insertion(inputList, elem):
    if not checkAvailable(inputList):
        raise ValueError

    if len(inputList) == 0:
        return [elem]
    elif elem > max(inputList):
        return inputList + [elem]
    elif elem < min(inputList):
        return [elem] + inputList
    else:
        output = inputList
        i = 0
        while i < len(inputList):
            if elem < output[i]:
                output = output[:i] + [elem] + output[i:]
                return output
            else:
                i += 1


def MergeSort(inputList):
    if not checkAvailable(inputList):
        raise ValueError

    if len(inputList) > 1:
        subLeft = inputList[:len(inputList) // 2]
        subRight = inputList[len(inputList) // 2:]

        MergeSort(subLeft)
        MergeSort(subRight)

        i = 0
        j = 0
        k = 0

        while i < len(subLeft) and j < len(subRight):
            if subLeft[i] < subRight[j]:
                inputList[k] = subLeft[i]
                i += 1
            elif subLeft[i] > subRight[j]:
                inputList[k] = subRight[j]
                j += 1
            k += 1

        while i < len(subLeft):
            inputList[k] = subLeft[i]
            i += 1
            k += 1

        while j < len(subRight):
            inputList[k] = subRight[j]
            j += 1
            k += 1

        output = inputList
        return output
    else:
        return inputList


def ShellSort(inputPart):
    if not checkAvailable(inputPart):
        raise ValueError

    inputList = inputPart
    medium = len(inputList) // 2
    while medium > 0:
        for i in range(medium, len(inputList)):
            temp = inputList[i]
            j = i
            while j >= medium and inputList[j - medium] > temp:
                inputList[j] = inputList[j - medium]
                j -= medium
            inputList[j] = temp
        medium //= 2
    return inputList


def QuickSort(inputList):
    if not checkAvailable(inputList):
        raise ValueError

    leftPart = []
    rightPart = []
    randomNum = inputList[random.randint(0, len(inputList) - 1)]

    while randomNum == max(inputList) or randomNum == min(inputList):
        randomNum = inputList[random.randint(0, len(inputList) - 1)]

    for i in inputList:
        if i < randomNum:
            leftPart += [i]
        elif i > randomNum:
            rightPart += [i]

    leftPart.sort()
    rightPart.sort()
    return leftPart + [randomNum] + rightPart
