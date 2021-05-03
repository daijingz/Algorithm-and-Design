# Expressions of Hiring problems
# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.co

class Hiring:
    def __init__(self, cost: int, cutoff: int, maxCost=100, minCost=0):
        if cost <= minCost:
            raise ValueError()
        elif cost >= maxCost:
            raise ValueError()
        elif minCost >= maxCost:
            raise ValueError()
        self.__cost = cost
        self.__applicants = []
        self.__cutoff = cutoff

    def __str__(self):
        Part1 = " Hiring problem "
        Part2 = " with cost " + str(self.__cost)
        if len(self.__applicants) == 0:
            Part3 = " without applicants "
        else:
            Part3 = " with applicants "
            for i in self.__applicants:
                Part3 += " " + str(i) + " "
        return Part1 + Part2 + Part3

    def getCost(self):
        return self.__cost

    def getApplicants(self):
        return self.__applicants

    def getCutoff(self):
        return self.__cutoff

    def addApplicants(self, app: int):
        self.__applicants = self.__applicants + [app]