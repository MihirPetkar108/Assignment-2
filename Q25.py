input_numbers = [1,2,3,4,5,6,7,8,9,10]

evenNumbers = list(filter(lambda x: x%2==0, input_numbers))
oddNumbers = list(filter(lambda x: x%2!=0, input_numbers))

print(f"Even Numbers: {evenNumbers}\nOdd Numbers: {oddNumbers}")
