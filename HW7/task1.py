from typing import Callable

names = ['Alex', 'Ihor', 'Agnieszka', 'Ivan']
func1 = lambda names: len(names) > 5

def custom_f(callback: callable, sequence):
    list = []
    type_sequence = type(sequence)
    for element in sequence:
        if callback(element):
            list.append(element)
    return type_sequence(list)


if __name__ == '__main__':
    print(custom_f(func1, names))