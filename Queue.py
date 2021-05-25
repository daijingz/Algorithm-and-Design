# Email Address: daij24@mcmaster.ca or david1147062956@163.com
class SettingError(Exception):
    """! Exception when setting values takes place"""
    pass


class Queue:
    def __init__(self, queue_size, head: int, tail: int):
        """! Initializes the program.

        @param
        @param
        @param

        """
        self.__queue = []
        i = 0
        while i < queue_size:
            self.__queue += [0]
            i += 1

        if head < 0 or tail < 0:
            raise Exception()
        elif head == tail:
            raise Exception()
        elif head >= len(self.__queue) or tail >= len(self.__queue):
            raise ValueError()
        self.__head = head
        self.__tail = tail

    def getQueue(self):
        try:
            return self.__queue
        except:
            raise Exception()

    def getHead(self):
        try:
            return self.__head
        except:
            raise Exception()

    def getTail(self):
        try:
            return self.__tail
        except:
            raise Exception()

    def enqueue(self, num: int):
        try:
            self.__queue[self.__tail] = num
            if self.__tail == len(self.__queue):
                self.__tail = 0
            else:
                self.__tail = self.__tail + 1
        except:
            raise SettingError()

    def dequeue(self):
        try:
            x = self.__queue[self.__head]
            if self.__head == len(self.__queue):
                self.__head = 0
            else:
                self.__head = self.__head + 1
            return x
        except:
            raise SettingError()