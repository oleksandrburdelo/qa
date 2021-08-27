from typing import Type

def singleton(_class: Type):
    def inner(*args):
        if not hasattr(_class, "_instance"):
            setattr(_class, "_instance", _class(*args))
            return getattr(_class, "_instance")
        return inner