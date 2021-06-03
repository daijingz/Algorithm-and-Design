# Author: Jingze Dai
# Date: 21/05/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import numpy
import statistics
from scipy import stats


class ML_Input:
    def __init__(self):
        """! Setting an empty tree with a central node (including values) """
        self.__data = []

    def getData(self):
        """! Get data values """
        try:
            return self.__data
        except:
            raise Exception()

    def addData(self, data: int):
        """! Add data values """
        try:
            self.__data = self.__data + [data]
        except:
            raise Exception()

    def Mean(self):
        """! Find mean values """
        return statistics.mean(self.getData())

    def ownMean(self):
        """! Own function about finding mean values """
        if len(self.__data) == 0:
            return 0
        input1 = self.getData()
        sum1 = sum(input1)
        return sum1/len(input1)

    def Median(self):
        """! Find median values """
        return numpy.median(self.getData())

    def ownMedian(self):
        """! Own function about finding median values """
        input1 = self.getData()
        input1.sort()
        if len(input1) % 2 == 0:
            median1 = len(input1) // 2
            median2 = len(input1) // 2 + 1
            return (input1[median1] + input1[median2])/2
        else:
            median = len(input1) // 2
            return input1[median]

    def Mode(self):
        """! Find mode values """
        return stats.mode(self.getData())

    def ownMode(self):
        """! Own function about finding mode values """
        occur = 0
        output = None
        for i in self.getData():
            if self.getData().count(i) > occur:
                occur = self.getData().count(i)
                output = i
        return output