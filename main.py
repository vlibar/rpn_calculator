from rpn import infix_to_postfix
from tokenization import tokenize_expr
from calculation import calculate_rpn_expr
import re

if __name__ == '__main__':
    expr = input('Enter a mathematical expression:\n')
    token_list = tokenize_expr(expr)
    postfix_list = infix_to_postfix(token_list)
    print(calculate_rpn_expr(postfix_list))
