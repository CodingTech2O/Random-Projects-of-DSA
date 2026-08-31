score  = 0
password = input("Enter password, don't worry I won't steal it ")

for i in range(10):
    if str(i) in password:
        score+=25
        break
if password.lower() == password or password.upper() == password or all(char.isdigit() for char in password):
    pass
else:
    score+=20
if len(password) >= 10:
    score+=30
special_chars = "!@#$%^&*()_|}{:?><,./;'[]-=~`'"
for i in special_chars:
    if i in password:
        score+=25
        break
print(f"Your password strength is {score}")