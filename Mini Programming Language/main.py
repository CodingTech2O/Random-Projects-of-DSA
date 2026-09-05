from funcs import save_var,print_var,evaluate

vars = {}

while True:
    inp = input("")
    if "=" in inp:
        vars[save_var(inp, vars)[0]] = save_var(inp, vars)[-1]
    elif "PRINT" in inp:
        print("OUT: ", evaluate(print_var(inp), vars))