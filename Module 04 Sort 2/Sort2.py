# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Other interesting sorting methods

class OtherErrors(Exception):
    """! Exception for all other problems"""
    pass


def checkAvailable(inputList):
    """! Function Check whether it is correct and appropriate"""
    try:
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
    except:
        raise OtherErrors("Other errors founded.")


def heapify(array, n, i):
    """! heapSort helper function"""
    try:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and array[largest] < array[left]:
            largest = left

        if right < n and array[largest] < array[right]:
            largest = right

        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            heapify(array, n, largest)
    except:
        raise OtherErrors("Other errors founded.")


def heapSort(array):
    """! heapSort function"""
    try:
        n = len(array)

        for i in range(n // 2 - 1, -1, -1):
            heapify(array, n, i)

        for i in range(n - 1, 0, -1):
            array[i], array[0] = array[0], array[i]
            heapify(array, i, 0)
    except:
        raise OtherErrors("Other errors founded.")


def countingSort(array, expr):
    """! radixSort helper function"""
    try:
        n = len(array)
        output = [0] * n
        count = [0] * 50

        for i in range(0, n):
            index = array[i] // expr
            count[index % 10] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = array[i] // expr
            output[count[index % 10] - 1] = array[i]
            count[index % 10] -= 1
            i -= 1

        for i in range(0, len(array)):
            array[i] = output[i]
    except:
        raise OtherErrors("Other errors founded.")


def radixSort(array):
    """! radixSort function"""
    try:
        if len(array) <= 0:
            return []
        max1 = max(array)

        exp_num = 1
        while max1 / exp_num > 1:
            countingSort(array, exp_num)
            exp_num *= 10
    except:
        raise OtherErrors("Other errors founded.")


def insertionSort(array: list):
    """! bucketSort helper function"""
    try:
        for i in range(1, len(array)):
            up = array[i]
            j = i - 1
            while j >= 0 and array[j] > up:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = up
        return array
    except:
        raise OtherErrors("Other errors founded.")


def bucketSort(input_list: list):
    """! bucketSort function"""
    try:
        array = []
        slots = 10
        for i in range(slots):
            array.append([])

        for j in input_list:
            index_b = int(slots * j)
            array[index_b].append(j)

        for i in range(slots):
            array[i] = insertionSort(array[i])

        k = 0
        for i in range(slots):
            for j in range(len(array[i])):
                input_list[k] = array[i][j]
                k += 1
        return input_list
    except:
        raise OtherErrors("Other errors founded.")