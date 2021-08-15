# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Quick Find


class QuickFind:
    def __init__(self, number=0):
        """! QuickFind object constructor """
        try:
            number = int(number)
        except:
            raise Exception()
        finally:
            if number > 0:
                self.__length = number
                self.__points = [x for x in range(number)]
            else:
                self.__length = 10
                self.__points = [x for x in range(10)]

    def get_length(self):
        """! Getting objects' groups value """
        try:
            return self.__length
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
        try:
            return self.__points[p]
        except:
            raise Exception()

    def union(self, p, q):
        """! Union method """
        src = self.find(p)
        tgt = self.find(q)
        if src == tgt:
            return

        self.__length -= 1
        for i, v in enumerate(self.__points):
            if v == tgt:
                self.__points[i] = src

    def __len__(self):
        """! Return the amount of elements """
        try:
            return len(self.__points)
        except:
            raise Exception()

    def __str__(self):
        """! Return the string form of object """
        try:
            return "length: {0}; points: {1}".format(self.__length, self.__points)
        except:
            raise Exception()

    def __repr__(self):
        """! Return a printable representation of object """
        return str(self)

    def __eq__(self, other):
        """! Check 2 objects on whether they are equal """
        if isinstance(other, QuickFind):
            if self.__points == other.__points and self.__length == other.__length:
                return True
        return False