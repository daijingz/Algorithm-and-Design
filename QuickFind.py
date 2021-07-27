# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Quick Find


class QuickFind:
    def __init__(self, n):
        self.__groups = n
        self.__points = [x for x in range(n)]

    def get_groups(self):
        try:
            return self.__groups
        except:
            raise Exception()

    def get_points(self):
        try:
            return self.__points
        except:
            raise Exception()

    def is_connected(self, p, q):
        try:
            return self.find(p) == self.find(q)
        except:
            raise Exception()

    def find(self, p):
        try:
            return self.__points[p]
        except:
            raise Exception()

    def union(self, p, q):
        src = self.find(p)
        tgt = self.find(q)
        if src == tgt:
            return

        self.__groups -= 1
        for i, v in enumerate(self.__points):
            if v == tgt:
                self.__points[i] = src

    def __str__(self):
        try:
            return "groups: {0}; points: {1}".format(self.__groups, self.__points)
        except:
            raise Exception()

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, QuickFind):
            if self.__points == other.__points and self.__groups == other.__groups:
                return True
        return False