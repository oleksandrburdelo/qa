from typing import Callable

names = ['Alex', 'Ihor', 'Agnieszka', 'Ivan']
func1 = (lambda a, b: a + b)
func2 = (lambda a, b: a if a > b else b)
func3 = (lambda a, b: a if a < b else b)

def custom_r(callback: Callable, sequence):
    element = sequence[0]
    counter = 0
    for _ in sequence:
        if len(sequence) - 1 == counter:
            break
        counter += 1
        element = callback(element, sequence[counter])
    return element

if __name__ == '__main__':
    print(custom_r(func1, names))