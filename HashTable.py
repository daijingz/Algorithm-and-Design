# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: HashTable


class DirectedAddressTable:
    def __init__(self, length: int):
        """! Initialize the program"""
        if length < 0:
            raise Exception()
        self.__length = length
        self.__body = []
        i = 0
        while i < length:
            self.__body += [None]
    
    def get_length(self):
        """! Get the length value of object"""
        try:
            return self.__length
        except:
            raise Exception()

    def get_body(self):
        """! Get the body value of object"""
        try:
            return self.__body
        except:
            raise Exception()

    def direct_address_search(self, index: int):
        """! Search direct address"""
        try:
            if index < 0 or index >= self.__length:
                raise ValueError()
            return self.get_body()[index]
        except:
            raise Exception()

    def direct_address_insert(self, index: int, data):
        """! Insert direct address"""
        try:
            if index < 0 or index >= self.__length:
                raise ValueError()
            elif self.__body[index] is not None:
                raise ValueError()
            self.__body[index] = data
        except:
            raise Exception()

    def direct_address_delete(self, index: int):
        """! Delete direct address"""
        try:
            if index < 0 or index >= self.__length:
                raise ValueError()
            self.__body[index] = None
        except:
            raise Exception()