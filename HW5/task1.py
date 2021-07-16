from random import *
import os
import pickle

some_file = 'text.txt'
numbers = [tuple(result for result in [randint(1,1000), randint(1,1000), randint(1,3)]) for row in range(100)]  # too much overhead=)

os.makedirs('./test/test1')
os.chdir('test/test1')
os.system(f"touch {some_file}")

with open(some_file, 'wb') as file:
    data = pickle.dumps(numbers)
    file.write(data)

# Take a look how it could be written cleaner
# import pickle
# import os
#
# from random import randint
#
#
# os.makedirs("test/data")
# operations = []
#
# for _ in range(100):
#     operations.append((randint(1, 100), randint(1, 100), randint(1, 3)))
#
# with open("test/data/text.txt", "wb") as file:
#     pickle.dump(operations, file)
