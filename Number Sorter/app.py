numbers = [1,2,3,5,4,9,7]
new_numbers = []
def mini(numbers):
    minimum = None
    for i in range(len(numbers)):
        if minimum == None:
            minimum = numbers[i]
        if minimum > numbers[i]:
            minimum = numbers[i]
    print(minimum)
    return minimum
print(f"Initial List: {numbers}\n")
while len(numbers)!=0:
    minimum = mini(numbers)
    numbers.remove(minimum)  
    new_numbers.append(minimum)
    print(f"Old Numbers: {numbers}\n Sorted Numbers: {new_numbers}\n")
    

