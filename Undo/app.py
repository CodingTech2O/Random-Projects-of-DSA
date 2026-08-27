main = []
all = []
def show():
    string = ""
    for m in main:
        string = string+f"{m} "
    print(string)
while True:
    inp  = input("Type or Undo/Redo: ")
    if inp.lower() == "undo":
        main.pop()
        show()

    elif inp.lower() == "redo":
        copy = []
        for a in all:
            copy.append(a)
        main = copy
        show()

    else:
        main.append(inp)
        all.append(inp)
        show()
        