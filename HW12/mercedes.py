from HW12.car import Car
from HW12.carfunc import Functions


class Mercedes(Car, Functions):
    def __init__(self):
        self.__wheels = 4
        self.__engine = "Diesel Engine"
        self.__turbo = "Yes"
        self.__horsepower = "249hp"
        self.__body_type = "Wagon"
        self.__exhaust_system = "AMG exhaust system"
        self.__fuel_tank = 0
        self.__adblue = 0
        self.__headlights = True
        self.__frontlights = True
        self.__model = "C320 CDI W205"
        self.__brand = "Mercedes-Benz"

    @staticmethod
    def turn_on_engine(self):
        print("Press StartStop button for turn on engine")

    @staticmethod
    def turn_off_engine(self):
        print("Press StartStop button for turn off engine")

    @property
    def refuel_tank(self):
        if self.__fuel_tank < 80:
            self.__fuel_tank += 40
            print("Full fuel tank")
        else:
            print("You should fuel your tank")
        # TODO: getter should only return something but not modification

    @property
    def add_adblue(self):
        if self.__adblue == 10:
            print("Full adblue tank")
        else:
            print("Car say bye bye")
        # TODO: property getter should return something. I suggest to make this property like method

    @staticmethod
    def move(self):
        print("press gas pedal for acceleration")

    @staticmethod
    def stop(self):
        print("press brake pedal for stop")


# Good. I see inheritance hiding and incapsulation. But incapsulation in getter should not modificate state of object but just return something
