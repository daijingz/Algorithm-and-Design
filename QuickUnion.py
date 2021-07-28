# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Quick Union


class QuickUnion:
    def __init__(self, n):
        """! QuickUnion object constructor """
        self.__groups = n
        self.__points = [x for x in range(n)]

    def get_groups(self):
        """! Getting objects' groups value """
        try:
            return self.__groups
        except:
            raise Exception()

    def get_points(self):
        """! Getting objects' points value """
        try:
            return self.__points
        except:
            raise Exception()

    def is_connected(self, p, q):
        """! Check 2 parts of an object about whether they are connected or not """
        try:
            return self.find(p) == self.find(q)
        except:
            raise Exception()

    def find(self, p):
        """! Find method """
        while p != self.__points[p]:
            p = self.__points[p]
        return p

    def union(self, p, q):
        """! Union method """
        parent = self.find(p)
        child = self.find(q)
        if parent == child:
            return

        self.__groups -= 1
        self.__points[child] = parent

    def __str__(self):
        """! Return the string form of object """
        return "groups: {0}; points: {1}".format(self.__groups, self.__points)

    def __repr__(self):
        """! Return a printable representation of object """
        return str(self)

    def __eq__(self, other):
        """! Check 2 objects on whether they are equal """
        if isinstance(other, QuickUnion):
            if self.__points == other.__points and self.__groups == other.__groups:
                return True
        return False