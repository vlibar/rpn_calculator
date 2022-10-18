import re


def tokenize_expr(expr):
    split_str = re.split(r' *([\(\)\+\-\*\^/]) *', expr)
    return list(filter(None, split_str))
