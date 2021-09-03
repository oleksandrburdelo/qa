from HW14.task.human import Human

if __name__ == '__main__':
    james = Human("James", 11, "dancing")
    john = Human("John", 39, "swimming")
    marta = Human("Marta", 28, "running")
    alex = Human("Alex", 5, "eating")

    people = [james, john, marta, alex]

    for human in people:
        print(human.action())

# take a look on alternative solution
