# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com


class Table:
    def __init__(self, row: int, col: int):
        if row <= 0 or col <= 0:
            raise Exception()
        elif row >= 20 or col >= 20:
            raise Exception()
        self.__row = row
        self.__col = col
        self.__index = 0
        self.__body = dict()

        built_index = 0
        rowAmount, colAmount = 0, 0

    def get_row(self):
        try:
            return self.__row
        except:
            raise Exception()

    def get_col(self):
        try:
            return self.__col
        except:
            raise Exception()

    def get_index(self):
        try:
            return self.__index
        except:
            raise Exception()

    def get_body(self):
        try:
            return self.__body
        except:
            raise Exception()

    def set_row(self):
        pass

    def set_col(self):
        pass

    def set_index(self):
        pass

    def set_point(self):
        pass

    def empty(self):
        pass

    def __str__(self):
        pass

    def appendRow(self):
        pass

    def deleteRow(self):
        pass

    def insertRow(self):
        pass

    def appendCol(self):
        pass

    def deleteCol(self):
        pass

    def insertCol(self):
        pass

    def filter(self):
        pass

    def rotate(self):
        pass