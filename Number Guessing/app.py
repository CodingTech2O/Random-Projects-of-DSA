import random
num = random.randint(1, 1000)
print("You have to guess a number between 1,1000")
print("You have 20 guesses\n")
for i in range(20):
    number = int(input("Enter your first guess: "))
    if number < num:
        print("Higher\n")
    elif number > num:
        print("Lower\n")
    if number == num:
        print("You won!\n\n")
        break
    