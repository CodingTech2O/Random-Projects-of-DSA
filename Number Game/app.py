import math

class no_range():
    def __init__(self,start,end):
        self.start = start
        self.end = end

x = 1
ran = None
while ran == None:
    question = input(f"Is your number less than {10**x}, Yes/No: ")
    if question.lower() == "yes":
        ran = no_range(1,10**x)
    else:
        x+=1
number = None
while number == None:
    question = input(f"Is your number less than or equal to {math.floor((ran.start+ran.end)/2)}, Yes/No: ")
    if question.lower() == "yes":
        ran.end = math.floor((ran.start+ran.end)/2)
        print(ran.start,ran.end)

    else:
        ran.start = math.floor((ran.start+ran.end)/2)
    if ran.end-ran.start ==2:
        question = input(f"Is your number {ran.end} Yes/No: ")
        if question.lower() == "yes":
            number = ran.end
        else:
            number = ran.end -1

print(f"Your number is: {number}")