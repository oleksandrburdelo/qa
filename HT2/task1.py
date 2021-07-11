global_logic = ['employee1', 'employee2', 'employee3']
toshiba = ['employee3', 'employee4', 'employee5']

new_employee = [global_logic, toshiba]
for employees in new_employee:
    for new_toshiba_employees in employees:
        print(new_toshiba_employees)