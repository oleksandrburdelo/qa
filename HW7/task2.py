from typing import Callable

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)
func1 = (lambda num: str(num))
func2 = (lambda num: str(num).title() )

def custom_m(callback: Callable, sequence):
    list = []
    type_sequence = type(sequence)
    for element in sequence:
        list.append(callback(element))
    return type_sequence(list)

if __name__ == '__main__':
    print(custom_m(func1, nums))