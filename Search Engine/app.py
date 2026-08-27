doc1 = "Python is a programming language".lower()
doc2 = "Python can be used for data science".lower()
doc3 = "Java is also a programming language".lower()
print(doc1,doc2,doc3)
found = {}

while True:
    results = []
    inp = input("Enter Keyword: ")
    inp = inp.lower()
    if inp in found.keys():
        results = found[inp]
        print(results)
    else:
        if inp in doc1:
            results.append("Doc 1")
        if inp in doc2:
            results.append("Doc 2")
        if inp in doc3:
            results.append("Doc 3")
        if not results:
            print("Keyword didn't match")
            break
        found[inp] = results
        print(results)