# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Bag basic Implementation


class Bag:
    def __init__(self):
        self.body = ()

    def add(self, item):
        new_body = self.body + (item, )
        self.body = new_body

    def isEmpty(self):
        return len(self.body) == 0

    def size(self):
        return len(self.body)