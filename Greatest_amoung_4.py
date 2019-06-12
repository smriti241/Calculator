no1 = int(input("First number: "))
no2 = int(input("Second number: "))
no3 = int(input("Third number: "))
no4 = int(input("Fourth number: "))
if no1 > no2:
    if no1 > no3:
        if no1 > no4:
            print(no1)
        else:
            print(no4)
    elif no3 > no4:
        print(no3)
    else:
        print(no4)
elif no2 > no3:
    if no2 > no4:
        print(no2)
    else:
        print(no4)
elif no3 > no4:
    print(no3)
else:
    print(no4)


