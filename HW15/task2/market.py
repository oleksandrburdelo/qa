from abc import abstractmethod

from HW15.task2.positions import Banana, Strawberry, Apple, Celery
from HW15.task2.product import Product


class Market:
    # @abstractmethod # well it could not be abstract since you have implementation. You should use static method
    @staticmethod  # -1 point
    def get_fruit(name: str) -> Product:
        if name == "banana":
            return Banana()
        elif name == "apple":
            return Apple()
        elif name == "celery":
            return Celery()
        elif name == "strawberry":
            return Strawberry()
        else:
            raise Exception("No position in shop")



if __name__ == '__main__':

    # 1 variant: (objects diplayed as same object)

    print(Market.get_fruit("banana"))
    print(Market.get_fruit("apple"))
    print(Market.get_fruit("celery"))
    print(Market.get_fruit("strawberry"))



    # 2 variant: (objects diplayed as different object)

    # banana = Market.get_fruit("banana")
    # apple = Market.get_fruit("apple")
    # cellery = Market.get_fruit("cellery")
    # strawberry = Market.get_fruit("strawberry")
    # print(banana)
    # print(apple)
    # print(cellery)
    # print(strawberry)

