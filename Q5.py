def name_average(students):
    student_Average = {}
    for student in students:

        name = student['name']
        math = student['math']
        science = student['science']
        english = student['english']

        averageMarks = round((math + science + english)/3,2)

        student_Average[name] = averageMarks
    
    return student_Average

students = [ {'name': 'Arjun', 'math': 85, 'science': 90, 'english': 78}, {'name': 'Balram',
'math': 92, 'science': 88, 'english': 84}, {'name': 'Damodar', 'math': 72, 'science': 75,
'english': 80} ]

print(name_average(students))