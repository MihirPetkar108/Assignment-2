def isPass(*marks):
    average_marks = int(sum(marks)/len(marks))

    if average_marks < 40:
        print("Fail")
    elif average_marks >= 40 and average_marks < 75:
        print("Pass")
    elif average_marks >= 75 and average_marks <= 100:
        print("Distinction")
    else:
        print("Enter valid marks")

maths,phy,chem,history,geography = map(int, input("Enter your marks(maths,phy,chem,history,geography) seperated by a ',': ").split(','))
isPass(maths,phy,chem,history,geography)