webs = []
current_web = ""
while True:
    web = input("Enter Wesbite to visit or inp 1 to go back or 2 to go back to the next current: ")
    if web == "1":
        for i in range(len(webs)):
            if webs[i] == current_web:
                if i != 0:
                    current_web = webs[i-1]  
                    print(current_web)    
                    break
                else:
                    print("No Further history")
    elif web == "2":
        for i in range(len(webs)):
            if webs[i] == current_web:
                if i != (len(webs)-1):
                    current_web = webs[i+1]  
                    print(current_web)    
                    break
                else:
                    print("No Further sites visited")
    else:
        webs.append(web)
        current_web = webs[-1]
        print(f"{current_web} was successfully added")
    


