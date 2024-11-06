original_list = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

palindrome_list = list(filter(lambda x: x == x[:: -1], original_list))

print(palindrome_list)