# Expressions of Hiring problems
# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.co

class Hiring:
    def __init__(self, cost: int, cutoff: int, benefit, maxCost=100, minCost=0):
        if cost <= minCost:
            raise ValueError()
        elif cost >= maxCost:
            raise ValueError()
        elif minCost >= maxCost:
            raise ValueError()

        self.__cost = cost
        self.__applicants = []
        self.__cutoff = cutoff
        self.__benefit = benefit

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
        try:
            return self.__cost
        except:
            raise Exception

    def getApplicants(self):
        try:
            return self.__applicants
        except:
            raise Exception

    def getCutoff(self):
        try:
            return self.__cutoff
        except:
            raise Exception

    def getBenefit(self):
        try:
            return self.__benefit
        except:
            raise Exception

    def addApplicants(self, app: int):
        if app <= 0:
            raise ValueError()
        self.__applicants = self.__applicants + [app]

    def HiringPerfect(self):
        cost = 0
        net = []
        for i in self.getApplicants():
            cost = cost + self.__cost
            net += [self.__benefit(i) - cost]
        return max(net)

    def Hiring(self, target):
        net = 0
        j = 0
        for i in self.__applicants:
            net -= self.__cost
            net += self.__benefit(i)
            j += 1
            if net >= target:
                break
        return j
