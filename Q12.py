def isInTuple(my_tuple, element_to_check):
    if element_to_check in my_tuple:
        print(f"{element_to_check} is in the tuple!")
    else:
        print(f"{element_to_check} is not in the tuple!")

my_tuple = (1, 2, 3, 4, 5, 'apple', 'banana')

element_to_check = input("Enter an element to check whether it is present in the tuple: ")

try:
    if element_to_check.isdigit():
        element_to_check = int(element_to_check)
except ValueError:
    pass

isInTuple(my_tuple, element_to_check)


