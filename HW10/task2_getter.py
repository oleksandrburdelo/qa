class Employee:

    def __init__(self,
                 first_name: str,
                 second_name: str,
                 age: str,
                 position: str,
                 birthday: str,
                 projects: str,
                 work_expirience: str):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.position = position
        self.birthday = birthday
        self.projects = projects
        self.work_expirience = work_expirience

    @property
    def get_first_name(self):
        return self.first_name

    @property
    def get_last_name(self):
        return self.last_name

    @property
    def get_age(self):
        return self.age

    @property
    def get_position(self):
        return self.position

    @property
    def get_bithday(self):
        return self.projects

    @property
    def get_work_expirience(self):
        return self.work_expirience

if __name__ == '__main__':
    Emp = Employee(
        'John',
        'Dow',
        '32',
        'Senior PM',
        '25.06.1989',
        'Medicine',
        '03.09.2017')
# Good code but it could be better if you will add state modification in some method -2 points
# also try to name properties not like actions
# @property
# def name(self):
#     return self.__name
