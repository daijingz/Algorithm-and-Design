# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Rod Cutting Problem
class RodCutting:
    def __init__(self, length: int, price: list):
        if length <= 0:
            raise Exception()

        self.__length = length

        if len(price) > length:
            raise Exception()
        elif price[0] <= 0:
            raise Exception()

        i = 0
        while i < len(price) - 1:
            if price[i] <= price[i + 1]:
                raise Exception()
            i += 1
        self.__price = price

    def get_length(self):
        try:
            return self.__length
        except:
            raise Exception()

    def get_price(self):
        try:
            return self.__price
        except:
            raise Exception()

    def empty_object(self):
        try:
            self.__length = 0
            self.__price = []
        except:
            raise Exception()

    def Cut_Rod(self):
        if self.__length == 0:
            return 0
        q = - 1000000
        i = 0
        while i < self.__length:
            self.__length = self.__length - i
            q = max(q, self.__price[i] + self.Cut_Rod())
            i += 1
        return q

    def Mem_Cut_Rod(self):
        i = 0
        r = []
        while i < self.__length:
            r += [- 1000000]
            i += 1
        return self.Mem_Cut_Rod_Aux(r)

    def Mem_Cut_Rod_Aux(self, r):
        if r[self.__length] > 0:
            return r[self.__length]
        if self.__length == 0:
            q = 0
        else:
            q = - 1000000
            j = 0
            while j < self.__length:
                self.__length = self.__length - j
                q = max(q, self.__price[j] + self.Mem_Cut_Rod_Aux(r))
        r[self.__length] = q
        return q

    def Bottom_Up_Cut_Rod(self):
        r = []
        r += [0]
        i = 0
        while i < self.__length:
            q = - 1000000
            j = 0
            while j < i:
                q = max(q, self.__price[i] + r[j - i])
                j += 1
            r[i] = q
            i += 1
        return r[self.__length]