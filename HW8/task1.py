def mathoperation(func):
    def inner(*args, **kwargs):
        func_name = func.__name__
        func_res = func(*args, **kwargs)
        print(func_name)
        return func_res
    return inner


@mathoperation
def Multiplication(number_one: {int}, number_two: {int}) -> {int}:
    result = number_one * number_two
    return result


@mathoperation
def Division(number_one: {int}, number_two: {int}) -> {int}:
    result = number_one // number_two
    return result


@mathoperation
def Int_Division(number_one: {int}, number_two: {int}) -> {int}:
    result = number_one / number_two
    return result


if __name__ == '__main__':
    print(5 + Multiplication(10, 4))
    print(Division(5, 3))
    print(Int_Division(25, 11))
    # Good. Names of functionsa and variables should be in lower case and snake case
