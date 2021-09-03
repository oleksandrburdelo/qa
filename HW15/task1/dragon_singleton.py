from typing import Type


def singleton(_class: Type):
    def inner(*args):
        if not hasattr(_class, "__instance"):
            setattr(_class, "__instance", _class(*args))
            return getattr(_class, "__instance")
    return inner
# Nice but instance in not private in your solution
# Python converts names to next format to make them private:
# _className__attributeName
# -2 points
