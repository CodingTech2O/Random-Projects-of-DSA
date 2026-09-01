text = input("Enter the text to analyze: ")

words = len(text.split())
avg_w_len = 0
x = 0
for t in text:
    if t != " ":
        x+=1
avg_w_len = round(x/words,2)
repeated = {}
characters = len(text)
characters_no_space = x
avg_reading_time = 250
reading_time = f"{round(words/250)} minutes"
for i in text.split():
    if i in repeated.keys():
        repeated[i] = repeated[i]+1
    else:
        repeated[i] = 1
sentences = len(text.split(".")) - 1
print("================ TEXT ANALYZER ===================")
print(f"Words {words}")
print(f"Characters {characters}")
print(f"Characters no spaces {characters_no_space}")
print(f"Sententces {sentences}")
print(f"Average Word Length {avg_w_len}")
print("Common Words \n")

for key,value in repeated.items():
    if value > 1:
        print(f"{key} - {value}")

print(f"Reading Time {reading_time}")



