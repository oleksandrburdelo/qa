numbers = [1, 2, 3, 4, 5, 6, 7, 8]
list_1 = []  # I suggest to name it like even_numbers
list_2 = []  # I suggest to name it like odd_numbers

for y in numbers:
    if y % 2 == 0:  # Well you are checking not an index but value so it is incorrect solution
        list_1.append(y)  # You should append tuple instead of element of list. list_1.append((index, value))
    else:
        list_2.append(y)

print(list_1)
print(list_2)

# Take a look on last link which I have provide for homework in links for lesson in LMS