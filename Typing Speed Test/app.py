import datetime

then = datetime.datetime.now()
text ="the quick brown fox jumped over the lazy dog"
print("Type", text)
inp = input("Enter your text here: ")
now = datetime.datetime.now()
inp = inp.lower().strip()
score = 0
i = 0
for _ in inp:
    
    if text[i] == inp[i]:
       score+=1
    i+=1
time = now - then
speed = (len(text.split(" "))/time.total_seconds())*60

print(f"Speed: {round(speed, 2)}WPM\nAccuracy: {round(score/i*100)}%")
