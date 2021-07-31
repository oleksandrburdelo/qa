def sum(operand1: int, operand2: int) -> int:
    return operand1 + operand2

def diff(operand1: int, operand2: int) -> int:
    return operand1 - operand2

def div(operand1: int, operand2: int) -> int:
    return operand1 / operand2

def mult(operand1: int, operand2: int) -> int:
    return operand1 * operand2

if __name__ == '__main__':
    print(sum(5, 10))
    print(diff(5, 10))
    print(div(5,10))
    print(mult(5, 10))