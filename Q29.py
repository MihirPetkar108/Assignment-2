def student_grades(grades):
    for marks in grades:
        grades[marks] = round((sum(grades[marks]) / len(grades[marks])),2)
        
    print(grades)

grades = {'Sat': [85, 90, 78],'Chid': [92, 88, 84],'Anand': [72, 75, 80]}
student_grades(grades)