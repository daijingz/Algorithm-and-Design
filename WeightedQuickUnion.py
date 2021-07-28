# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Weighted Quick Union


class WeightedQuickUnion:
    def __init__(self, n):
        """! WeightedQuickUnion object constructor """
        self.__groups = n
        self.__points = [x for x in range(n)]
        self.__weights = [1 for _ in range(n)]

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

    def get_weights(self):
        """! Getting objects' weights value """
        try:
            return self.__weights
        except:
            raise Exception()

    def is_connected(self, q, p):
        """! Check 2 parts of an object about whether they are connected or not """
        try:
            return self.find(p) == self.find(q)
        except:
            raise Exception()

    def find(self, p):
        """! Find method """
        if p == self.__points[p]:
            return p
        else:
            return self.find(self.__points[p])

    def union(self, p, q):
        """! Union method """
        parent = self.find(p)
        child = self.find(q)
        if parent == child:
            return

        self.__groups -= 1

        if self.__weights[child] <= self.__weights[parent]:
            self.__points[child] = parent
            self.__weights[parent] += self.__weights[child]
        else:
            self.__points[parent] = child
            self.__weights[child] += self.__weights[parent]

    def __str__(self):
        """! Return the string form of object """
        return 'points:{0},groups:{1},weights:{2}'.format(self.__points, self.__groups, self.__weights)

    def __repr__(self):
        """! Return a printable representation of object """
        return str(self)

    def __eq__(self, other):
        """! Check 2 objects on whether they are equal """
        if isinstance(other, WeightedQuickUnion):
            if self.__points == other.__points and self.__groups == other.__groups and self.__weights == other.__weights:
                return True
        return False