class DrivingLicense:
    def __init__(self, age):
        self.__age = age
        self.__value = None

    def __get__(self, instance, owner):
        return instance.__dict__[self.__age]

    def __set__(self, instance, value):
        if value >= 16:
            self.__value = f'you can get driving license and drive rent or own car'
            instance.__dict__[self.__age] = self.__value
        else:
            self.__value = (f"you can't drive car cause you are young, you have to "
                            f"wait {abs(value - 16)} {f'years' if 16 - value > 1 else f'year'}")
            instance.__dict__[self.__age] = self.__value