# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# This file includes programs with 4 different kinds of sorting algorithm
# All of those target inputs are lists consist of unrepeated integers and floats
# Sort output is ascending-integer list
import random


class InappropriateInput(Exception):
    """! Exception when inputs are inappropriate"""
    pass


def checkAvailable(inputList):
    """! Function Check whether it is correct and appropriate"""
    i = 0
    while i < len(inputList):
        if not isinstance(inputList[i], (float, int)):
            return False
        i += 1

    for j in inputList:
        if inputList.count(j) > 1:
            return False
        elif j == 0:
            return False

    return True


def SelectionSort(inputList):
    """! Sort select the minimum and make it into the new array again and again"""
    if not checkAvailable(inputList):
        raise InappropriateInput()

    output = []
    loopList = inputList
    while len(loopList) > 0:
        output += [min(loopList)]
        loopList.remove(min(loopList))
    return output


def InsertionSort(inputList):
    """! Sort select elements from left to right and insert them sequentially"""
    if not checkAvailable(inputList):
        raise InappropriateInput()

    output = []
    for i in inputList:
        output = Insertion(output, i)
    return output


def Insertion(inputList, elem):
    """! Find the right place for an element in a sorted list"""
    if not checkAvailable(inputList):
        raise InappropriateInput()

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
    """! Divide list into sub-lists and sort them, then combine their results together"""
    if not checkAvailable(inputList):
        raise InappropriateInput()

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
    """! Variation of Insertion Sort"""
    if not checkAvailable(inputPart):
        raise InappropriateInput()

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
    """! Find a comparable index (not max or min) and then compare others"""
    if not checkAvailable(inputList):
        raise InappropriateInput()

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
