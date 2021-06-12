# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com


class Table:
    def __init__(self, x: int, y: int):
        if x <= 0 or y <= 0:
            raise Exception()
        elif x >= 20 or y >= 20:
            raise Exception()
        self.__x = x
        self.__y = y

        self.__body = []
        i, j = 0, 0
        while i < x:
            arr = []
            while j < y:
                arr += [0]
                j += 1
            j = 0
            self.__body += [arr]
            i += 1

    def get_x(self):
        try:
            return self.__x
        except:
            raise Exception()

    def get_y(self):
        try:
            return self.__y
        except:
            raise Exception()

    def get_body(self):
        try:
            return self.__body
        except:
            raise Exception()

    def set_x(self, x: int):
        if x <= 0 or x >= 20:
            raise Exception()
        self.__x = x

    def set_y(self, y: int):
        if y <= 0 or y >= 20:
            raise Exception()
        self.__y = y

    def set_point(self, x: int, y: int, value: int):
        if x > self.__x:
            raise Exception()
        elif y > self.__y:
            raise Exception()
        elif value <= 0:
            raise Exception()

        row, col = x - 1, y - 1
        self.__body[row][col] = value

    def empty(self):
        self.__body = []
        i, j = 0, 0
        while i < self.__x:
            arr = []
            while j < self.__y:
                arr += [0]
                j += 1
            j = 0
            self.__body += [arr]
            i += 1

    def __str__(self):
        output = ""
        for i in self.__body:
            index = 0
            while index < len(i):
                if index == len(i) - 1:
                    output += str(i[index]) + "\n"
                else:
                    output += str(i[index]) + " "
                index += 1
        return output

    def appendRow(self, row=None):
        if row is None:
            row = []

        try:
            if type(row) != list:
                raise Exception()
            if not row:
                rowNum = self.__x
                i = 0
                newRow = []
                while i < rowNum:
                    newRow += [0]
                    i += 1
                self.__body += [newRow]
            elif len(row) == self.__x:
                self.__body += [row]
            else:
                raise Exception()
        except:
            raise Exception()

    def deleteRow(self, number: int):
        if number <= 0 or number > self.__x:
            raise Exception()
        value = []
        i = 0
        while i < len(self.__body):
            if i != number:
                value += [self.__body[i]]
            i += 1
        self.__x = self.__x - 1
        self.__body = value

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