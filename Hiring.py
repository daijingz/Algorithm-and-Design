# Expressions of Hiring problems
# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.co

class Hiring:
    def __init__(self, cost, maxCost=100, minCost=0):
        if cost <= minCost:
            raise ValueError()
        elif cost >= maxCost:
            raise ValueError()
        self.cost = cost
        self.applicants = []

    def __str__(self):
        Part1 = " Hiring problem "
        Part2 = " with cost " + str(self.cost)
        if len(self.applicants) == 0:
            Part3 = " without applicants "
        else:
            Part3 = " with applicants "
            for i in self.applicants:
                Part3 += " " + str(i) + " "
        return Part1 + Part2 + Part3

    def getCost(self):
        return self.cost

    def getApplicants(self):
        return self.applicants