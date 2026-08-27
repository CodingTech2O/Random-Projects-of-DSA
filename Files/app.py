import os
import shutil

path = input(r"Enter path to folder: ")
files = os.listdir(path)

for file in files:
    filename, extention = os.path.splitext(file)
    extention = extention[1:]
    if os.path.exists(f"{path}/{extention}"):
        shutil.move(f"{path}/{file}",f"{path}/{extention}/{file}")
    else:
        os.mkdir(f"{path}/{extention}")
        shutil.move(f"{path}/{file}",f"{path}/{extention}/{file}")

print("Done! ")