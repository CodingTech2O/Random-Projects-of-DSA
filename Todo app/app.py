todo = []
while True:
    inp = input("Enter a command (add, list): ").strip().lower()
    inp = inp.split(" ", 1)
    if inp[0] == "add":
        task = inp[1:]
        if task:
            todo.append(task)
            print(f"Added: {task}")
        else:
            print("No task provided.")
    elif inp[0] == "list":
        if todo:
            print("Tasks:")
            for i in range(len(todo)):
                print(f"{i + 1}. {todo[i]}")
        else:
            print("No tasks in the list.")