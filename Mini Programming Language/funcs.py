def check_if_var_defined_in_inp(inp):
    if "=" in inp:
        return True
    return False
def save_var(inp, vars):
    if check_if_var_defined_in_inp(inp):
        var_name = inp.split("=")[0].strip()
        var_value = str(evaluate(inp.split("=")[1].strip(), vars))
        return [var_name,var_value]
    return []
def check_if_print_in_inp(inp):
    if "PRINT" in inp:
        return True
    return False
def print_var(inp):
    if check_if_print_in_inp(inp):
        return inp.split("PRINT")[-1]
    return ""

import re

def evaluate(expression, vars):
    for v in vars:
        expression = re.sub(r"\b" + re.escape(v) + r"\b", vars[v], expression)

    try:
        return eval(expression)
    except:
        return expression