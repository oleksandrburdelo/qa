from drivinglicense import DrivingLicense, Action


# class Human:
#     __age = DrivingLicense("age")  # It should not be descriptor.
#
#     def __init__(self, name: str, age: int):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def getlicense(self):
#         return f"{self.__name}, {self.__age }"
#
#
class Human:
    def __init__(self, name: str, age: int, action_name: str):
        self.__name = name
        self.__age = age
        self.__action = Action(action_name)

    @property
    def action(self):
        return self.__action
