# Expressions of Hiring problems
# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.co

class Hiring:
    def __init__(self, cost: int, cutoff: int, benefit, maxCost=100, minCost=0):
        """! Initializes the program.

        @param cost     average cost when have a interview with an applicant
        @param cutoff   the edge where the applicant reaches requirements of company
        @param benefit  function for calculating the benefits of applicants
        @param maxCost  maximum number of costs
        @param minCost  minimum number of costs

        @return A model of Hiring problems with different parameters

        """
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
        """! Returns a description string of Hiring object"""
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
        """! Getters for returning object's cost value'"""
        try:
            return self.__cost
        except:
            raise Exception

    def getApplicants(self):
        """! Getters for returning object's applicant list"""
        try:
            return self.__applicants
        except:
            raise Exception

    def getCutoff(self):
        """! Getters for returning object's cutoff values"""
        try:
            return self.__cutoff
        except:
            raise Exception

    def getBenefit(self):
        """! Getters for returning object's benefit functions"""
        try:
            return self.__benefit
        except:
            raise Exception

    def addApplicants(self, app: int):
        """! Add applicants to object's applicant list"""
        if app <= 0:
            raise ValueError()
        self.__applicants = self.__applicants + [app]

    def HiringPerfect(self):
        """! Hiring problem's solution"""
        try:
            cost = 0
            net = []
            for i in self.getApplicants():
                cost = cost + self.__cost
                net += [self.__benefit(i) - cost]
            return max(net)
        except:
            raise Exception()

    def Hiring(self, target):
        """! Hiring problem's solution in non-perfect situation"""
        try:
            net = 0
            j = 0
            for i in self.__applicants:
                net -= self.__cost
                net += self.__benefit(i)
                j += 1
                if net >= target:
                    break
            return j
        except:
            raise Exception()