import pickle

with open('./test/test1/text.txt', 'rb') as file:
    text1 = file.read()
    text2 = pickle.loads(text1)

for text3 in text2:
    print(text3)

# good but you should print each operation
# Also not clear names of variables take a look how it could be solved cleaner
# Not bad but it could be solved in more elegant way
# import pickle
#
# with open('test/data/text.txt', "rb") as file:
#     operations = pickle.load(file)
#
# for operation in operations:
#     left, right, operator = operation
#     if operator == 1:
#         print(f"{left} + {right} = {left + right}")
#     elif operator == 2:
#         print(f"{left} * {right} = {left * right}")
#     else:
#         print(f"{left} / {right} = {left / right}")
