class Table:
    def __init__(self, x: int, y: int):
        if x <= 0 or y <= 0:
            raise Exception()
        self.__x = x
        self.__y = y

        self.__body = []
        i, j = 0, 0
        while i < x:
            arr = []
            while j < y:
                arr += [None]
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