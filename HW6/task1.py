def arithmetic(left_operand, right_operand, operation):
    """
        Apply arithmetic operation for provided left and right operands
    """

    if (operation == '+'):
        return(left_operand + right_operand)
    elif (operation == '-'):
        return (left_operand - right_operand)
    elif (operation == '*'):
        return (left_operand * right_operand)
    elif (operation == '/'):
        return (left_operand / right_operand)
    return f'Not known operation: {operation}'

# Good but double quotes is preferable in docstrings instead of single quotes
# if (operation == '+') - well it is good but square braces are excessive here.
# if operation == '+' - more preferable
