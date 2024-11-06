def pattern():
    for i in range(5):
        for j in range(i+1,6):
            print(j,end=" ")

        print(" ",end= "")

        for j in range(1, i+2):
            print(j,end= " ")

        print()

pattern()