def even_numbers(my_list):
    for i in my_list:
        if i%2 != 0:
            continue
        print(f"{i}, ", end="")

my_list = [1, 2, 3, 4, 5, 6]

even_numbers(my_list)