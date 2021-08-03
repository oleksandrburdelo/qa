class GlobalLogic:

    def __init__(self,
                 name: str,
                 founded: int,
                 ceo: str,
                 employees: int,
                 branches: int,
                 countries: float,
                 website: str):
        self.__name = name
        self.__founded = founded
        self.__ceo = ceo
        self.__employees = employees
        self.__branches = branches
        self.__countries = countries
        self.__website = website
    @property
    def get_name(self):
        return self.__name

    @property
    def get_founded(self):
        return self.__founded

    @property
    def key_people(self):
        return self.__ceo

    @property
    def employees(self):
        return self.__employees

    @property
    def branches(self):
        return self.__branches

    @property
    def countries(self):
        return self.__countries

    @property
    def get_website(self):
        return self.__website

if __name__ == '__main__':
    gl = GlobalLogic(
        "Name: GlobalLogic",
        "Founded: 2000",
        "CEO: Shashank Samant",
        "Employees: 27.000,",
        "Branches: 11",
        "Countries: Ukraine, USA, Slovakia, Sweden, Croatia, Poland, Germany, Canada, Israel, India, Argentina",
        "WebSite: https://www.globallogic.com/")
