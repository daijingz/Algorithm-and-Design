# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com


class MaximumSubarray:
    def __init__(self, dailyPrice, startPrice=100):
        if type(startPrice) != int:
            raise TypeError()
        elif startPrice < 0:
            raise ValueError()
        elif type(dailyPrice) != list:
            raise TypeError()
        elif dailyPrice[0] != startPrice:
            raise ValueError()

        self.startPrice = startPrice
        self.dailyPrice = dailyPrice
        self.net = []
        for i in self.dailyPrice:
            self.net += [i - self.startPrice]

    def BruteForce(self):
        i = 0
        j = 0
        netIncome = 0
        dayNum1 = 0
        dayNum2 = 0

        while i < len(self.dailyPrice) - 1:
            while j < len(self.dailyPrice):
                if self.net[j] - self.net[i] > netIncome:
                    netIncome = self.net[j] - self.net[i]
                    dayNum1 = i
                    dayNum2 = j
                j += 1
            i += 1
            j = i

        output = (dayNum1, dayNum2)
        return output

    # An algorithm which is an expression of Greedy Algorithm
    def MaxAndMin(self):
        sequence = self.net
        sequence.sort()
        i = 0
        j = len(sequence) - 1

        output = 0
        while j > 0:
            while i < j:
                if sequence.index(sequence[i]) < sequence.index(sequence[j]):
                    if sequence[j] - sequence[i] > output:
                        output = sequence[j] - sequence[i]
                i += 1
            if i == j:
                i = 0
                j -= 1
        return output

    def DivideAndConquer(self):
        middlePoint = len(self.net) // 2
        inputL = self.net
        inputL.sort()
        leftPart = inputL[:middlePoint]
        rightPart = inputL[middlePoint:]

        output = 0
        i = 0
        j = len(rightPart) - 1
        while j > 0:
            while i < j:
                if self.net.index(leftPart[i]) < self.net.index(rightPart[j]):
                    if rightPart[j] - leftPart[i] > output:
                        output = rightPart[j] - leftPart[i]
                i += 1
            if i == j:
                i = 0
                j -= 1
        return output