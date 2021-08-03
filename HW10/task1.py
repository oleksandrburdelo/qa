class GlobalLogic:

    def __init__(self,
                 name: str,
                 founded: int,
                 ceo: str,
                 employees: int,
                 branches: int,
                 countries: float,
                 website: str):

        self.name = name
        self.founded = founded
        self.ceo = ceo
        self.employees = employees
        self.branches = branches
        self.countries = countries
        self.website = website

    def get_name(self):
        return self.name

    def get_founded(self):
        return self.founded

    def key_people(self):
        return self.ceo
    
    def employees(self):
        return self.employees

    def branches(self):
        return self.branches

    def countries(self):
        return self.countries

    def get_website(self):
        return self.website

gl_description: GlobalLogic = GlobalLogic(
    "Name: GlobalLogic",
    "Founded: 2000",
    "CEO: Shashank Samant",
    "Employees: 27.000,",
    "Branches: 11",
    "Countries: Ukraine, USA, Slovakia, Sweden, Croatia, Poland, Germany, Canada, Israel, India, Argentina",
    "WebSite: https://www.globallogic.com/")

print(gl_description.name)
print(gl_description.founded)
print(gl_description.ceo)
print(gl_description.employees)
print(gl_description.branches)
print(gl_description.countries)
print(gl_description.website)
