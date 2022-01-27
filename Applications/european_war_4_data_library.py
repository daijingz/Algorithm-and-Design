class data_library:
    def __init__(self):
        self.__terrains = dict()
        self.__general_rank = [5, 10, 25, 20, 28, 36, 44, 54, 64, 74, 86, 98, 110, 125, 150]
        self.__general_skills = dict()
        self.__city_cost = (65, 0)
        self.__city_benefits = [(3, 0), (6, 0), (12, 0), (20, 2), (30, 4), (45, 6), (67, 8)]
        self.__factory_cost = (60, 20)
        self.__factory_benefits = [(0, 4), (0, 8), (0, 12), (0, 16)]
        self.__stable_cost = (80, 5)
        self.__stable_benefits = [(3, 0), (6, 0), (9, 0)]
        self.__farm_cost = (40, 0)
        self.__farm_benefits = [5, 15, 40]
        self.__harbour_cost = (75, 10)
        self.__harbour_benefits = []

    def get_terrains(self):
        try:
            return self.__terrains
        except:
            raise Exception()

    def get_general_rank(self):
        try:
            return self.__general_rank
        except:
            raise Exception()

    def get_general_skills(self):
        try:
            return self.__general_skills
        except:
            raise Exception()

    def get_city_cost(self):
        try:
            return self.__city_cost
        except:
            raise Exception()

    def get_city_benefits(self):
        try:
            return self.__city_benefits
        except:
            raise Exception()

    def get_factory_cost(self):
        try:
            return self.__factory_cost
        except:
            raise Exception()

    def get_factory_benefits(self):
        try:
            return self.__factory_benefits
        except:
            raise Exception()

    def get_stable_cost(self):
        try:
            return self.__stable_cost
        except:
            raise Exception()

    def get_stable_benefits(self):
        try:
            return self.__stable_benefits
        except:
            raise Exception()

    def get_farm_cost(self):
        try:
            return self.__farm_cost
        except:
            raise Exception()

    def get_farm_benefits(self):
        try:
            return self.__farm_benefits
        except:
            raise Exception()