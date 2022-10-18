import sys


def not_greater(i, j):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    try:
        a = precedence[i]
        b = precedence[j]
        return True if a <= b else False
    except KeyError:
        return False


def infix_to_postfix(tokenized_expr):
    operator_list = ['+', '-', '*', '/']
    output_lst = []
    stack = []
    for elem in tokenized_expr:
        try:
            output_lst.append(float(elem))
        except ValueError:
            if elem == '(':
                stack.append('(')
            elif elem == ')':
                try:
                    while stack[-1] != '(':
                        output_lst.append(stack.pop())
                    stack.pop()
                except IndexError:
                    print('В введённом выражении не совпадает количество открытых и закрытых скобок')
                    sys.exit()
            elif elem in operator_list:
                while stack and not_greater(elem, stack[-1]):
                    output_lst.append(stack.pop())
                stack.append(elem)
            else:
                print('Некорректный ввод. Выражение может содержать только целые (123) и дробные числа (13.45), '
                      'скобки, операции +, -, /, * ')
                sys.exit()
    while stack:
        output_lst.append(stack.pop())
    return output_lst
