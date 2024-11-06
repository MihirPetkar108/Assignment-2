def character_type(string):
    for i in string:
        match True:
            case _ if(i.isupper()):
                print(f"{i}: Is an uppercase!")
            case _ if(i.islower()):
                print(f"{i}: Is a lowercase!")
            case _ if(i.isdigit()):
                print(f"{i}: Is a digit!")
            case _ :
                print(f"{i}: It is something else!")

string = str(input("Enter a string: "))
character_type(string)