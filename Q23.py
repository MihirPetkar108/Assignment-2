def isPrime(n):
    for i in range(2,int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

print("Enter a number to find whether it is a Prime or a composite number (Enter '-1' to exit):")

while(True):
    n = int(input("Enter a number: "))

    if n == -1:
        print("End of Program!")
        break
    if isPrime(n):
        print(f"{n} is a Prime Number!")
    else:
        print(f"{n} is a Composite Number!")
