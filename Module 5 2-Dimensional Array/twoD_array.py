# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: 2-dimensional array implementation 1
class IllegalPointValue(Exception):
    pass


class twoD_array:
    def __init__(self, x: int, y: int):
        """!
        @param x    number of rows
        @param y    number of columns
        """
        if x <= 0 or y <= 0:
            raise ValueError("Error: x and y should between 1 and 20")
        elif x > 20 or y > 20:
            raise ValueError("Error: x and y should between 1 and 20")
        self.__x = x
        self.__y = y

        self.__body = []
        i, j = 0, 0
        while i < x:
            subarray = []
            while j < y:
                subarray += [0]
                j += 1
            j = 0
            self.__body += [subarray]
            i += 1

    def get_x(self):
        """! Getting x values"""
        try:
            return self.__x
        except:
            raise Exception()

    def get_y(self):
        """! Getting y values"""
        try:
            return self.__y
        except:
            raise Exception()

    def get_body(self):
        """! Getting body values"""
        try:
            return self.__body
        except:
            raise Exception()

    def set_x(self, x: int):
        """! Setting x values"""
        if x <= 0 or x > 20:
            raise ValueError("Error: x should between 1 and 20")
        self.__x = x

    def set_y(self, y: int):
        """! Setting y values"""
        if y <= 0 or y > 20:
            raise ValueError("Error: y should between 1 and 20")
        self.__y = y

    def set_point(self, x: int, y: int, value: int):
        """! With given coordinates, insert values inside"""
        if x > self.__x:
            raise ValueError("Error: x not in the range")
        elif y > self.__y:
            raise ValueError("Error: y not in the  range")
        elif value <= 0:
            raise IllegalPointValue("Error: Point value should be non-negative integer value")

        row, col = x - 1, y - 1
        self.__body[row][col] = value

    def empty(self):
        self.__body = []
        i, j = 0, 0
        while i < self.__x:
            subarray = []
            while j < self.__y:
                subarray += [0]
                j += 1
            j = 0
            self.__body += [subarray]
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

    def insertRow(self, index: int, row=None):
        if row is None:
            row = []

        try:
            if type(row) != list:
                raise Exception()
            elif index <= 0:
                raise Exception()

            if index > self.__x:
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
            else:
                if not row:
                    rowNum = self.__x
                    i = 0
                    newRow = []
                    while i < rowNum:
                        newRow += [0]
                        i += 1
                elif len(row) == self.__x:
                    newRow = row
                else:
                    raise Exception()

                output = []
                i = 0
                while i < len(self.__body):
                    if index == i:
                        output += [newRow]
                    output += [self.__body[i]]
                    i += 1
                self.__body = output
        except:
            raise Exception()

    def appendCol(self, col=None):
        try:
            if col is None:
                new_col = []
                i = 0
                while i < self.__y:
                    new_col += [0]
            elif len(col) == self.__y:
                new_col = col
            else:
                raise Exception()

            j = 0
            output = []
            while j < self.__y:
                output = self.__body[j] + [new_col[j]]
                j += 1
            self.__body = output
        except:
            raise Exception()

    def deleteCol(self):
        try:
            output = []
            for i in self.__body:
                if len(i) > 0:
                    output += [i[:-1]]
                else:
                    output += [[]]
            self.__body = output
        except:
            raise Exception()

    def insertCol(self):
        pass

    def filter(self):
        pass

    def rotate(self):
        pass

    def checkRow(self):
        pass

    def checkCol(self):
        pass