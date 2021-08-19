class MercedesBenz:

    def __init__(self):
        self.__wheels = 4
        self.__engine = "Diesel Engine"
        self.__turbo = "Yes"
        self.__horsepower = "249hp"
        self.__body_type = "Wagon"
        self.__exhaust_system = "AMG exhaust system"
        self.__fuel_tank = 85
        self.__adblue = 10
        self.__headlights = "LED headlights"
        self.__frontlights = "LED front lights"
        self.__model = "C320 CDI W205"
        self.__brand = "Mercedes-Benz"

    def __clear(self, item) -> str:
        result = item.replace(f"_{self.__class__.__name__}__", "")
        return result

    def __str__(self):
        res = ""
        for key, value in self.__dict__.items():
            res += f"{self.__clear(key)}: {value}\n\t"
        return (
            f"{self.__class__.__name__}:{{\n"
            f"\n\t{res}\n}}"
        )
