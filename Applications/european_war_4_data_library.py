class data_library:
    def __init__(self):
        self.__terrains = dict()
        self.__general_skills = dict()
        self.__city_cost = (65, 0)
        self.__city_benefits = [(3, 0), (6, 0), (12, 0), (20, 2), (30, 4), (45, 6), (67, 8)]
        self.__factory_cost = (60, 20)
        self.__factory_benefits = [(0, 4), (0, 8), (0, 12), (0, 16)]
        self.__stable_cost = (80, 5)
        self.__factory_benefits = [(3, 0), (6, 0), (9, 0)]
        self.__farm_cost = (40, 0)
        self.__farm_benefits = []