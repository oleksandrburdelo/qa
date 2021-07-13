from random import *
import os
import pickle

some_file = 'text.txt'
numbers = [tuple(result for result in [randint(1,1000), randint(1,1000), randint(1,3)]) for row in range(100)]

os.makedirs('./test/test1')
os.chdir('test/test1')
os.system(f"touch {some_file}")

with open(some_file, 'wb') as file:
    data = pickle.dumps(numbers)
    file.write(data)