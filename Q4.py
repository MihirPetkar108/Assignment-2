def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

print("Enter numbers to find total number of even and odd numbers(press 'R' to show the result):")

evenNumberCount = 0
oddNumberCount = 0

while True:
    userInput = input("Enter a number: ")

    if userInput == 'R':
        break

    try:
        num = int(userInput)
        if (isEven(num)):
            evenNumberCount += 1    
        else:
            oddNumberCount += 1
    
    except ValueError:
        print("Please enter a valid number or 'R' to show the result.")

print(f"Even Number Count: {evenNumberCount}\nOdd Number Count: {oddNumberCount}")
