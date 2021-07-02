# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Binary Search Tree (BST)


class Leaf:
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        try:
            return self.__value
        except:
            raise Exception()