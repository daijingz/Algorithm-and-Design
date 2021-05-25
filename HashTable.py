# Author: Jingze Dai
# Date: 25/05/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
from collections import defaultdict


class DirectedAddressTable:
    def __init__(self, length: int):
        if length < 0:
            raise Exception()
        self.__length = length
        self.__body = []
        i = 0
        while i < length:
            self.__body += [None]

    def get_length(self):
        try:
            return self.__length
        except:
            raise Exception()

    def get_body(self):
        try:
            return self.__body
        except:
            raise Exception()

    def direct_address_search(self, index: int):
        try:
            if index < 0 or index >= self.__length:
                raise ValueError()
            return self.get_body()[index]
        except:
            raise Exception()

    def direct_address_insert(self, index: int, data):
        try:
            if index < 0 or index >= self.__length:
                raise ValueError()
            elif self.__body[index] is not None:
                raise ValueError()
            self.__body[index] = data
        except:
            raise Exception()

    def direct_address_delete(self, index: int):
        try:
            if index < 0 or index >= self.__length:
                raise ValueError()
            self.__body[index] = None
        except:
            raise Exception()