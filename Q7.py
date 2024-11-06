def factorialNumber(num):
    if num == 0:
        return 1
    
    factorial = num * factorialNumber(num-1)

    return factorial

num = 5
print(factorialNumber(num))