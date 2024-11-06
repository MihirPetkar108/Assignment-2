def print_except_multiple_5():
    for i in range(1,21):
        if i % 5 == 0:
            continue
        else:
            print(i)

print_except_multiple_5()