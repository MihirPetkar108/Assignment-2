def decimal_to_binary(n):
    binary = ''

    if n == 0:
        return 0
    
    while n > 0:
        binary = str(n%2) + binary
        n //= 2
    
    return binary

n = int(input("Enter a decimal number to convert it to binary: "))
binaryNumber = decimal_to_binary(n)
print(f"{n} to binary number is {binaryNumber}")