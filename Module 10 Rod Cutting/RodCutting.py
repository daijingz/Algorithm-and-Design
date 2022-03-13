# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Rod Cutting Problem


class Rod:
    def __init__(self, length: int, price: list):
        """!
        Construct a Rod object for rod cutting algorithm
        @:param length      length of rod
        @:param price       price list of different length's rods
        """
        if length <= 0:
            raise Exception()

        self.__length = length

        if len(price) > length:
            raise Exception()
        elif price[0] <= 0:
            raise Exception()

        i = 0
        while i < len(price) - 1:
            if price[i] >= price[i + 1]:
                raise Exception()
            i += 1
        self.__price = price

    def get_length(self):
        """! @return length of Rod object """
        try:
            return self.__length
        except:
            raise Exception()

    def get_price(self):
        """! @return price list of Rod object """
        try:
            return self.__price
        except:
            raise Exception()

    def set_rod(self, length: int, price: list):
        """! Reset rod values"""
        self.__length = length

        if len(price) > length:
            raise Exception()
        elif price[0] <= 0:
            raise Exception()

        i = 0
        while i < len(price) - 1:
            if price[i] >= price[i + 1]:
                raise Exception()
            i += 1
        self.__price = price

    def empty_object(self):
        """! Empty a rod object """
        try:
            self.__length = 0
            self.__price = []
        except:
            raise Exception()

    def __eq__(self, other):
        """! Compare 2 Rod objects to check whether they are equal """
        if isinstance(other, Rod):
            return self.__length == other.__length and self.__price == other.__price
        return False

    def Cut_Rod(self):
        """! Cut rod algorithm implementations """
        if self.__length <= 0:
            return 0
        q, i = 0, 0
        length = self.__length
        price = self.__price
        while i < self.__length:
            self.__length = self.__length - i - 1
            q = max(q, self.__price[i] + self.Cut_Rod())
            i += 1
            self.__length = length
            self.__price = price
        return q

    def Mem_Cut_Rod(self):
        """! Memorized cut rod algorithm implementations """
        i = 0
        r = []
        while i < self.__length:
            r += [0]
            i += 1
        return self.Mem_Cut_Rod_Aux(r)

    def Mem_Cut_Rod_Aux(self, r):
        """! Helper function of memorized cut rod algorithm implementations """
        if self.__length < len(r) and r[self.__length] > 0:
            return r[self.__length]
        if self.__length <= 0:
            q = 0
        else:
            q = - 1000000
            j = 0
            length = self.__length
            price = self.__price
            while j < self.__length:
                self.__length = self.__length - j - 1
                q = max(q, self.__price[j] + self.Mem_Cut_Rod_Aux(r))
                j += 1
                self.__length = length
                self.__price = price
        r += [q]
        return q

    def analysis(self):
        """! Rod cutting problem analyzing """
        i = 0
        output = []
        while i < len(self.__price):
            output += [self.__price[i] / (i + 1)]
            i += 1
        output.sort()
        return output