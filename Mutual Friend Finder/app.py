friends = {
    "Aditya": ["Akshat", "Rahul"],
    "Akshat": ["Aditya", "Riya"],
    "Rahul": ["Aditya", "Riya"],
    "Riya": ["Akshat", "Rahul"]
}

while True:
    f1 = input("Person 1:")
    f2 = input("Person 2:")
    mf = []
    for i in friends[f1]:
        if i in friends[f2]:
            mf.append(i)
    print(mf)