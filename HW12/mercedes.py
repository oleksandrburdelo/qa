from HW12.car import Car
from HW12.carfunc import Functions


class Mercedes(Car, Functions):
    def __init__(self):
        self._wheels = 4
        self._engine = "Diesel Engine"
        self._turbo = "Yes"
        self._horsepower = "249hp"
        self._body_type = "Wagon"
        self._exhaust_system = "AMG exhaust system"
        self._petrol_tank = True
        self._headlights = True
        self._frontlights = True
        self._model = "C320 CDI W205"
        self._brand = "Mercedes-Benz"