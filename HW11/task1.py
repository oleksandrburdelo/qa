from abc import ABC


class Foundation_of_Car(ABC):
    def __int__(self):
        # region TODO: this fields could be protected to share only with child
        self.wheels = 4
        self.engine = True
        self.body_type = True
        self.exhaust_system = True
        self.fuel_tank = True
        self.headlights = True
        self.frontlights = True
        # endregion

    # region TODO: incorrect usage of static methods
    @staticmethod
    def moving_streight(self):
        print("Moving forward")

    @staticmethod
    def moving_back(self):
        print("move back")

    @staticmethod
    def turning_right(self):
        print("turn right")

    @staticmethod
    def turning_left(self):
        print("turn left")

    @staticmethod
    def stop(self):
        print("stop")
    # endregion

    # region TODO: better to use abstract method decorator
    def engine_work(self):
        raise NotImplementedError("not implemented")

    def environmental_impact(self):
        raise NotImplementedError("not implemented")

    def refuel_car(self):
        raise NotImplementedError("not implemented")
    # endregion


class DieselCar(Foundation_of_Car):
    def __init__(self):
        super().__init__()
        # region TODO: this fields should be protected
        self.wheels = 4
        self.body_type = "Wagon or Sedan"
        self.engine = "Diesel"
        self.fuel_economy = "l/100 km"
        self.exhaust_system = True
        # endregion

    def acceleration_diesel(self):
        print("acceleration from 0 to 50 km/h")

    def refuel_tank_diesel(self):
        print("car fueling on gas station")


class PetrolCar(Foundation_of_Car):
    def __init__(self):
        super().__init__()
        # region TODO: this fields should be protected
        self.wheels = 4
        self.body_type = "Wagon or Sedan"
        self.engine = "Petrol"
        self.exhaust_system = True
        # endregion

    def acceleration_petrol(self):
        print("acceleration from 0 to 50 km/h")

    def refuel_tank_petrol(self):
        print("car fueling on gas station")


class MB_C_Class(DieselCar):
    def __init__(self, model: str, body_type: str, engine_type: str, fuel_economy: str, doors: str):
        # TODO: constructor of Dielsel car does not used so all fields declired iinside Dielsel car missed
        # region TODO: this fields could be private since not used outside of class
        self.model = model
        self.body_type = body_type
        self.engine_type = engine_type
        self.fuel_economy = fuel_economy
        self.doors = doors
        # endregion


class Ford_Mustang(PetrolCar):
    def __init__(self, model: str, body_type: str, engine_type: str, fuel_economy: str, doors: str):
        # TODO: constructor of petroll does not used so all fields declired iinside petroll missed
        # region TODO: this fields could be private since not used outside of class
        self.model = model
        self.body_type = body_type
        self.engine_type = engine_type
        self.fuel_economy = fuel_economy
        self.doors = doors
        # endregion


if __name__ == '__main__':
    Diesel = MB_C_Class('W204', 'Wagon', 'OM654', '6.3 l/100 km', '5 doors')
    Petrol = Ford_Mustang('Made at 2005', 'Coupe', 'Engine 6,2', '20 l/100km', '2 doors')


