def generate_random_number(num1,num2):
    squared_number_list = []
    for i in range(num1, num2+1):
        square_number = i**2
        squared_number_list.append(square_number)

    return squared_number_list

def first_last_square_numbers(square_numbers):
    first_five_square_numbers = square_numbers[:5]
    last_five_square_numbers = square_numbers[-5:]

    return first_five_square_numbers, last_five_square_numbers

square_numbers = generate_random_number(1,30)

first_five_square_numbers, last_five_square_numbers = first_last_square_numbers(square_numbers)

print(f"First Five Square Numbers: {first_five_square_numbers}")
print(f"Last Five Square Numbers: {last_five_square_numbers}")