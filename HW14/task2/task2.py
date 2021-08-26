class ITR:
    def __init__(self, sequence: list, start: int, stop: int, step=1):
        self.__sequence = sequence
        self.__start = start
        self.__stop = stop
        self.__step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start < self.__stop - 1:
            item = self.__sequence[self.__start]
            if self.__step > 1:
                self.__start += self.__step
            else:
                self.__start += self.__step
            return item
        else:
            raise StopIteration