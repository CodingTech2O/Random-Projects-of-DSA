"""
        
word_list = []
while True:
    print("=====================================================================")
    print("1. Insert Word")
    print("2. Search Word")
    print("3. Exit")
    print("=====================================================================")
    inp = input("1/2/3: ")

    if inp == "1":
        word = input("Insert: ")
        word_list.append(word.lower())
    elif inp == "2":
        search = input("Search: ")
        if search.lower() in word_list:
            print("Word Found")
        else:
            print("Couldn't find word")
    elif inp == "3":
        break
    else:
        print("Didn't recognise that command")"""
words = [
    "python",
    "pygame",
    "pyramid",
    "pycharm",
    "apple",
    "application"
]
while True:
    words_matched = []
    inp = input("Enter prefix: ")
    for w in words:
        x = 0
        for i in range(len(inp)):
            n = list(w)
            inp = list(inp)
            if n[i] == inp[i]:
                x+=1
        if x == len(inp):
            words_matched.append(w)
    if len(words_matched) == 0:
        print("No Suggestions found. \n")
    else:
        print("Words matched: \n")
        for w in words_matched:
            print(w)
