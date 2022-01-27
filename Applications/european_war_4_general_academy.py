class academy:
    def __init__(self):
        self.__star_one_general = dict()
        self.__star_two_general = dict()
        self.__star_three_general = dict()
        self.__refresh = 2
        self.__refresh_present = 0

    def get_star_one_general(self):
        try:
            return self.__star_one_general
        except:
            raise Exception()