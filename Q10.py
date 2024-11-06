def isCurzonNumber(num):
    num1 = 1 + (2**num)
    num2 = 1 + (2*num)

    if(num1 % num2 == 0):
        print("The given number", num, "is a Curzon Number!")
    else:
        print("The given number", num, "is not a Curzon Number!")

num = int(input("Enter a number to find if it is a Curzon Number: "))
isCurzonNumber(num)