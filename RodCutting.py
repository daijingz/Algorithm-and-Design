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