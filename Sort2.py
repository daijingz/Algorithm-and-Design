# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Other interesting sorting methods
# Imported: TODO


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


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    r = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    elif r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

    return arr


def heapSort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        ele = arr[i]
        arr[i] = arr[0]
        arr[0] = ele
        heapify(arr, i, 0)


def countingSort(arr, exp1):
    n = len(arr)

    output = [0] * n

    count = [0] * 10

    for i in range(0, n):
        index = (arr[i] / exp1)
        count[int(index % 10)] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[int(index % 10)] - 1] = arr[i]
        count[int(index % 10)] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10


def InsertionSort(inputList):
    if not checkAvailable(inputList):
        raise ValueError

    output = []
    for i in inputList:
        output = Insertion(output, i)
        print(output)
    return output


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


def bucketSort(x):
    arr = []
    slot_num = 10
    for i in range(slot_num):
        arr.append([])

    for j in x:
        index_b = int(slot_num * j)
        arr[index_b].append(j)

    for i in range(slot_num):
        arr[i] = InsertionSort(arr[i])

    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
    return x