def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True
        
def primeNumbers(n):
    for i in range(2,n+1):
        if isPrime(i):
            print(f"{i} is Prime!")

n = int(input("Enter a number to find Prime Numbers till the entered number: "))
primeNumbers(n)