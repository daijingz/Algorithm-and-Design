class Leaf:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        try:
            return self.__value
        except:
            raise Exception()