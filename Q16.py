def age_category(age):
        if(age >=0 and age <=12):
            print("Child")
        elif(age >= 13 and age <= 19):
            print("Teenager")
        elif(age >= 20 and age <= 59):
            print("Adult")
        elif(age >= 60 and age <= 110):
            print("Senior")
        elif(age>110):
            pass
        else:
            print("Error: Please enter a valid number for age")
        
age = int(input("Enter your age: "))
age_category(age)