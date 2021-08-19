from OleksandrBurdelo.qa.HW13.task2.train import Train
from OleksandrBurdelo.qa.HW13.task2.train_car import TrainCar

if __name__ == '__main__':
    train = Train()
    train_car = TrainCar(105, 25, ['Oleksandr'])
    train.add_train_car(train_car)
    train_car.add_passenger(5)
    print(train_car)
    # Well could not add new passenger. Maybe it is not integer ? -3 points
