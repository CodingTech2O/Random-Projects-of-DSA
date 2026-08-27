print("===============================Contact Search===============================\n")
print("1. Add Contact")
print("2. Search Contact")
print("3. Show All Contacts")
print("4. Exit \n")
print("=============================================================================\n\n\n")
contacts = []
while True:
    inp = input("Choose 1-4 ")
    if inp == "1":
        contacts.append([input("Enter the name: "), input("Enter the number: ")])
    if inp == "2":
        found = False
        comparisions = 0
        name = input("Enter the name of person: ")
        for c in contacts:
            comparisions += 1
            if c[0].lower() == name.lower():
                print(f"Found {name}'s contact {c[1]}")
                print(f"Number of comparisons made: {comparisions}")
                found = True
                break
        if not found:
            print("Contact not found.")
    if inp == "3":
        print("Name | Contact No \n")
        for c in contacts:
            print(f"{c[0]} | {c[1]}")

    if inp == "4":
        break