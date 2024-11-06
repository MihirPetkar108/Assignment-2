my_list1 = [1,2,3,4,5,6,7,8,9,10]

my_list2 = list(map(lambda x: x**2, my_list1))
print(my_list2)

my_list3 = list(filter(lambda x: x%2 == 0, my_list1))
print(my_list3)