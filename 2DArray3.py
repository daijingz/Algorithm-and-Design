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

    def get_row(self):
        return self.__row

    def get_col(self):
        return self.__col