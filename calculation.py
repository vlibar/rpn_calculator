import sys


def calculate_rpn_expr(token_lst):
    ops = {
        "+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: a / b)
    }
    stack = []

    for token in token_lst:
        if token in ops:
            try:
                arg2 = stack.pop()
                arg1 = stack.pop()
                result = ops[token](arg1, arg2)
            except IndexError:
                print('Некорретное выражение, операторов больше, чем операндов')
                sys.exit()
            except ZeroDivisionError:
                print('Некорретное выражение, попытка деления на 0')
                sys.exit()
            stack.append(result)
        else:
            stack.append(token)
    return stack.pop()
