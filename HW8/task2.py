def func_square():
    square = ((item ** 2 for item in range(0, 1000000000) if item % 2 == 0))
    return square


for square1 in func_square():
    print(square1)

# Welll it will work but I want to see generator comprehension or generator function
# 2 points
