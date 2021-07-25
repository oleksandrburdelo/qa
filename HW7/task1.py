from typing import Callable


def custom_f(callback: Callable, sequence):
    list = []  # never name variables with existing names of types
    type_sequence = type(sequence)
    for element in sequence:
        if callback(element):
            list.append(element)
    return type_sequence(list)


if __name__ == '__main__':
    print(custom_f(lambda item: item > 5, [4, 5, 6, 7]))
# Not bad but spend amore time for naming and annotations and docstrings
