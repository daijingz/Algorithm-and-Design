# Jingze Dai Date: 2020/09/22
# Part 3 Algorithm: Approximation Algorithm on Vertex Cover
# Undirected graphs are represented as "Approximation_Graph" object
class Leaf:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        try:
            return self.__value
        except:
            raise Exception()