# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com

"""! Example Input: [100, 95, 105, 110, 120, 130]"""
"""! Where 100 is the price on the first day"""


class InAppropriateData(Exception):
    pass


class MaximumSubarray:
    def __init__(self, dailyPrice: list, startPrice=100):
        """! Initializes the program.

        @param dailyPrice   daily prices on stock markets (list of prices)
        @param startPrice   price at the beginning of trades (price)
        @param net          if people buy stock at the beginning day, how many benefits each day has (list of benefits)

        """
        if type(startPrice) != int:
            raise TypeError()
        elif startPrice < 0:
            raise ValueError()
        elif type(dailyPrice) != list:
            raise TypeError()
        elif dailyPrice[0] != startPrice:
            raise ValueError()
        elif len(dailyPrice) < 2:
            raise ValueError()

        self.__startPrice = startPrice
        self.__dailyPrice = []
        for i in dailyPrice:
            self.__dailyPrice += int(i)

        self.__net = []
        for j in self.__dailyPrice:
            self.__net += [j - self.__startPrice]

    def setStartPrice(self, number: int):
        self.__startPrice = number

    def getStartPrice(self, printed=True):
        if printed:
            print("Start Price: " + str(self.__startPrice))
        return self.__startPrice

    def emptyDailyPrice(self):
        self.__dailyPrice = []

    def getDailyPrice(self, printed=True):
        if printed:
            print("Daily Price: " + str(self.__dailyPrice))
        return self.__dailyPrice

    def getNet(self, printed=True):
        if printed:
            print("Net Price: " + str(self.__net))
        return self.__net

    def checkAvailable(self):
        for i in self.getDailyPrice():
            if i <= 0:
                return False
            elif type(i) not in [int, float]:
                return False
        return True

    def BruteForce(self):
        if not self.checkAvailable():
            raise InAppropriateData()

        if len(self.getDailyPrice(False)) == 0:
            return 0, 0

        i = 0
        j = 0
        netIncome = 0
        dayNum1 = 0
        dayNum2 = 0

        while i < len(self.__dailyPrice) - 1:
            while j < len(self.__dailyPrice):
                if self.__net[j] - self.__net[i] > netIncome:
                    netIncome = self.__net[j] - self.__net[i]
                    dayNum1 = i
                    dayNum2 = j
                j += 1
            i += 1
            j = i

        output = (dayNum1, dayNum2)
        return output

    # An algorithm which is an expression of Greedy Algorithm
    def MaxAndMin(self):
        if not self.checkAvailable():
            raise InAppropriateData()

        if len(self.getDailyPrice(False)) == 0:
            return 0, 0

        sequence = self.__net
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
        if not self.checkAvailable():
            raise InAppropriateData()

        if len(self.getDailyPrice(False)) == 0:
            return 0, 0

        middlePoint = len(self.__net) // 2
        inputL = self.__net
        inputL.sort()
        leftPart = inputL[:middlePoint]
        rightPart = inputL[middlePoint:]

        output = 0
        i = 0
        j = len(rightPart) - 1
        while j > 0:
            while i < j:
                if self.__net.index(leftPart[i]) < self.__net.index(rightPart[j]):
                    if rightPart[j] - leftPart[i] > output:
                        output = rightPart[j] - leftPart[i]
                i += 1
            if i == j:
                i = 0
                j -= 1
        return output


def fibonacci(n: int):
    if n < 0:
        raise InAppropriateData()
    elif n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacciM(n: int):
    memo = [1, 1]
    limit = n
    for i in range(3, limit + 1):
        memo.append(memo[i - 1] + memo[i - 2])
    return memo[-1]
