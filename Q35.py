def pass_students(grades, Min_marks):
    return list(filter(lambda x: x>Min_marks, grades))

def curve_grades(grades):
    return list(map(lambda x: x + 5, grades))

def average_pass_students(grades):
    if len(grades) == 0:
        return 0

    if  len(grades) == 1:
        return grades[0]

    return (grades[0] + (len(grades) - 1 * average_pass_students(grades[1:]))) / len(grades)

def final_output(grades, Min_marks):
    grades = pass_students(grades, Min_marks)
    print(f"The grades of passed students: {grades}")
    grades = curve_grades(grades)
    print(f"Grades after curve: {grades}")
    print(f"Average marks of the pass students: {round(average_pass_students(grades), 2)}")


grades = [55,78,90,45,67,82,88] 
Min_marks_to_pass = 60
final_output(grades, Min_marks_to_pass)