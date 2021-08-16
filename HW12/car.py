from abc import ABC, abstractmethod


class Car(ABC):

        @staticmethod
        def turn_on_engine(self):
            print('Engine noise')

        @staticmethod
        def turn_off_engine(self):
            print('without engine noise')

        @staticmethod
        def refuel_tank(self):
            print("Fuel tank on gas station")

        @staticmethod
        def add_adblue(self):
            print("Fuel addblue tank on service")


        @abstractmethod
        def move(self):
            """Car move"""
            pass

        @abstractmethod
        def stop(self):
            """Car stop"""
            pass

