from drivinglicense import DrivingLicense

class Human:
    __age = DrivingLicense("age")

    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    @property
    def getlicense(self):
        return f"{self.__name}, {self.__age }"