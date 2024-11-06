def pattern():
    for i in range(6):
        for j in range(i):
            print("*",end=" ")
        print()

    for i in reversed(range(5)):
        for j in range(i):
            print("*",end =" ")
        print()

pattern()