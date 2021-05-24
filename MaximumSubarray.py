# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com


class InAppropriateData(Exception):
    """! Exception when function receives unexpected type data"""
    pass


class Bull(Exception):
    """! Exception when stock price is always rising"""
    pass


class Bear(Exception):
    """! Exception when stock price is always falling"""
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
            self.__dailyPrice += [int(i)]

        self.__net = []
        for j in self.__dailyPrice:
            self.__net += [j - self.__startPrice]

    def setStartPrice(self, number: int):
        """! Setting start price value"""
        self.__startPrice = number

    def getStartPrice(self, printed=True):
        """! Getting start price value"""
        try:
            if printed:
                print("Start Price: " + str(self.__startPrice))
            return self.__startPrice
        except:
            raise Exception

    def emptyDailyPrice(self):
        """! Setting daily price values to an empty list"""
        self.__dailyPrice = []

    def addDailyPrice(self, price):
        """! Adding new daily price value"""
        if type(price) not in [int, float]:
            raise InAppropriateData()
        self.__dailyPrice += [price]

    def getDailyPrice(self, printed=True):
        """! Getting daily price values"""
        try:
            if printed:
                print("Daily Price: " + str(self.__dailyPrice))
            return self.__dailyPrice
        except:
            raise Exception()

    def emptyNet(self):
        """! Setting net price values to an empty list"""
        self.__net = []

    def addNet(self, price):
        """! Adding new net price value"""
        if type(price) not in [int, float]:
            raise InAppropriateData()
        self.__net += [price]

    def getNet(self, printed=True):
        """! Getting net price values"""
        try:
            if printed:
                print("Net Price: " + str(self.__net))
            return self.__net
        except:
            raise Exception()

    def checkAvailable(self):
        """! Check whether an object is an appropriate object"""
        if self.__startPrice <= 0:
            return False
        elif self.__startPrice >= max(self.__dailyPrice):
            raise Bull()
        elif self.__startPrice <= min(self.__dailyPrice):
            raise Bear()

        for i in self.getDailyPrice():
            if i <= 0:
                return False
            elif type(i) not in [int, float]:
                return False
        return True

    def BruteForce(self):
        """! Checking every situation and find the most profitable one"""
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

    def MaxAndMin(self):
        """! Checking from best situations to find a most-profitable situation"""
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
        """! Dividing it into small sub-problems and solve them"""
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
    """! Divide and Conquer"""
    if n < 0:
        raise InAppropriateData()
    elif n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacciM(n: int):
    """! Divide and Conquer with Memorization"""
    memo = [1, 1]
    limit = n
    for i in range(3, limit + 1):
        memo.append(memo[i - 1] + memo[i - 2])
    return memo[-1]