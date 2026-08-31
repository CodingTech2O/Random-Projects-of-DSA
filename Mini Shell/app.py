commands = ["help", "calc","echo","exit"]
while True:
    cmd = input("MyShell> ")
    cmd = cmd.split(" ")
    if cmd[0] in commands:
        if cmd[0] == commands[0]:
            print(f"Commands are:\n{commands}")
        elif cmd[0] == commands[1]:
            print(eval(cmd[1]))
        elif cmd[0] == commands[2]:
            print(" ".join(cmd[1:]))
        elif cmd[0] == commands[3]:
            print("Goodbye.")
            break
    else:
        print("Command not found. Type help for list of commands")
