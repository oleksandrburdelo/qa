from HW15.task1.dragon_singleton import singleton


@singleton
class Dragon:
    def __init__(self,
                 type: str,
                 eyes: str,
                 limbs: str,
                 tail: str,
                 wings: str,
                 teeth: str,
                 bones: str,
                 color: str):

        self.__type = type
        self.__eyes = eyes
        self.__limbs = limbs
        self.__tail = tail
        self.__wings = wings
        self.__teeth = teeth
        self.__bones = bones
        self.__color = color

    @property
    def type(self):
        return self.__type

    @property
    def eyes(self):
        return self.__eyes

    @property
    def limbs(self):
        return self.__limbs

    @property
    def tail(self):
        return self.__tail

    @property
    def wings(self):
        return self.__wings

    @property
    def teeth(self):
        return self.__teeth

    @property
    def bones(self):
        return self.__bones

    @property
    def color(self):
        return self.__color



