from typing import List

from HW13.task2.train_car import TrainCar


class Train:
    def __init__(self):
        self.__train_cars = []

    def add_train_car(self, train_car: TrainCar):
        self.__train_cars.append(train_car)

    @property
    def train_cars(self):
        return self.__train_cars
