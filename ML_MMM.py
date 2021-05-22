# Author: Jingze Dai
# Date: 21/05/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import numpy
import statistics
from scipy import stats


class ML_Input:
    def __init__(self):
        self.__data = []

    def getData(self):
        return self.__data

    def addData(self, data: int):
        self.__data = self.__data + [data]

    def Mean(self):
        return statistics.mean(self.getData())

    def Median(self):
        return numpy.median(self.getData())

    def Mode(self):
        return stats.mode(self.getData())