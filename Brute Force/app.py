import random
password = "1235"

for i in range(10000):
    if len(str(i)) <4:
        to_fill = 4 - len(str(i))
        guess = "0"*to_fill + str(i)
    else:
        guess = str(i)
    if guess == password:
        print("Password is: " + guess)
        break
    print("Guessing: " + guess)