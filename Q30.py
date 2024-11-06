def square_numbers(numbers_list):
    numbers_list = list(map(lambda x: x**2, numbers_list))
    return numbers_list


print(square_numbers([1, 2, 3, 4]))