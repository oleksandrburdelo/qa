class TrainCar:
    def __init__(self, number_car: int, seats_in_car: int, passengers: list):
        self.__seats_in_car = seats_in_car
        self.__passengers = passengers
        self.__number_car = number_car

    def add_passenger(self, passengers: int):
        if len(self.__seats_in_car) <= len(self.__passengers + passengers):
            self.__passengers.append(passengers)
        else:
            print("There is no free seats in train")

    @property
    def __len__(self):
        return len(self.__passengers)

    @property
    def number_car(self):
        return self.__number_car

    @property
    def passengers(self):
        return self.__passengers

    @property
    def seats_in_car(self):
        return self.__seats_in_car

    def __str__(self):
        return f'[{self.__number_car}]'