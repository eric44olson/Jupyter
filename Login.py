names = []
namenum = len(names)
while namenum <= 3: 
    namein0 = input("Enter Name: ")
    names.append(namein0)
    namenum = len(names)
    print(names)

    namein1 = input("Enter Name: ")
    names.append(namein1)
    namenum = len(names)
    print(names)

print(namenum)
