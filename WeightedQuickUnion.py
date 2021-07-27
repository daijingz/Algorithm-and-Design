# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Weighted Quick Union


class WeightedQuickUnion:
    def __init__(self, n):
        self.__groups = n
        self.__points = [x for x in range(n)]
        self.__weights = [1 for _ in range(n)]

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

    def get_weights(self):
        try:
            return self.__weights
        except:
            raise Exception()

    def is_connected(self, q, p):
        return self.find(p) == self.find(q)

    def find(self, p):
        if p == self.__points[p]:
            return p
        else:
            return self.find(self.__points[p])

    def union(self, p, q):
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
        return 'points:{0},groups:{1},weights:{2}'.format(self.__points, self.__groups, self.__weights)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, WeightedQuickUnion):
            if self.__points == other.__points and self.__groups == other.__groups and self.__weights == other.__weights:
                return True
        return False