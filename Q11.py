def lowerUpperCase(string):
    upperCase_Count = 0
    lowerCase_Count = 0

    for character in string:
        if character.isupper():
            upperCase_Count += 1
        elif character.islower():
            lowerCase_Count += 1

    return [upperCase_Count, lowerCase_Count]

string = str(input("Enter a sentence to check the number of UpperCase and LowerCase: "))

upperCase_Count, lowerCase_Count = lowerUpperCase(string)

print(f"Uppercase Letters: {upperCase_Count}, Lowercase Letters: {lowerCase_Count}")