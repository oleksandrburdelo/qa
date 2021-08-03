class Employee:

    def __init__(self,
                 name: str,
                 surname: int,
                 age: int,
                 position: str,
                 birthday: float,
                 projects: str,
                 work_expirience: str):

        self.name = name
        self.surname = surname
        self.age = age
        self.position = position
        self.birthday = birthday
        self.projects = projects
        self.work_expirience = work_expirience


    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_age(self):
        return self.age

    def get_position(self):
        return self.position

    def get_birhday(self):
        return self.birthday

    def get_projects(self):
        return self.projects

    def work_expirience(self):
        return self.work_expirience

employee1: Employee = Employee(
    'NameName: John',
    'Surname: Dow',
    'Age:32',
    'PositionName: Senior PM',
    'Birthday: 25.06.1989',
    'Projects: Medicine',
    'WorkExpirience: 03.09.2017')


print(employee1.name)
print(employee1.surname)
print(employee1.age)
print(employee1.position)
print(employee1.birthday)
print(employee1.projects)
print(employee1.work_expirience)
