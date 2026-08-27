numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
done = []
for i in numbers:
    if i not in done:
        found = -1
        for j in numbers:
            if i==j:
                found+=1
        print(f"{found} duplicate/duplicates found of {i}")
    done.append(i)