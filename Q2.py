def isEligible(*Score):
    totalScore = 0
    for i in Score:
        totalScore += i
    
    totalScore /= 5
    print("Average:",totalScore)

    if totalScore >= 85 and totalScore <= 100:
        print("Eligible for Scholarship")        
    elif totalScore >=75 and totalScore < 85:
        print("Waiting List")
    elif totalScore >=0 and totalScore < 75:
        print("Not Eligible")
    else:
        print("Invalid Input")

print("Input your Marks out of 100:-")
Phy = int(input("Enter marks of Physics: "))
Chem = int(input("Enter marks of Chemistry: "))
Maths = int(input("Enter marks of Maths: "))
English = int(input("Enter marks of English: "))
Social_Studies = int(input("Enter marks of Social Studies: "))

isEligible(Phy, Chem, Maths, English, Social_Studies)
