def average_salary_by_department(*Employees):
    department_salaries = {}
    for Employee_Details in Employees:
        department = Employee_Details["department"]
        salary = Employee_Details["salary"]

        if department not in department_salaries:
            department_salaries[department] = {"total_salary": 0, "count": 0}
        
        department_salaries[department]["total_salary"] += salary
        department_salaries[department]["count"] += 1

        salary_by_department = {}

        for department, details in department_salaries.items():
            total_salary = details["total_salary"]
            count = details["count"]
            salary_by_department[department] = round(total_salary/count, 2)
    
    return salary_by_department

def department_with_highest_salary(*Employees):
    average_salaries = average_salary_by_department(*Employees)

    highest_salary_department = max(average_salaries, key = average_salaries.get)
    highest_salary = average_salaries[highest_salary_department]

    return highest_salary_department, highest_salary

def youngest_employee_in_department(*Employees):
    youngest_employee = {}
    youngest_employee_checker = {}
    for employee_details in Employees:
        name = employee_details["name"]
        age = employee_details["age"]
        department = employee_details["department"]
        youngest_name
        youngest_age = 0
        youngest_department
        
        if youngest_age == 0:
            youngest_name = name
            youngest_age = age
            youngest_department = department
        elif youngest_age < age:
            youngest_name = name
            youngest_age = age
            youngest_department = department

        
            
    name = youngest_employee[department]["name"]
    age = youngest_employee[department]["age"]
    department = department

    return name, age, department
        

Employee1 = {"name": "Suresh", "age": 35, "salary": 25453.43, "department": "Engineer"}
Employee2 = {"name": "Aryan", "age": 28, "salary": 43572.34, "department": "HR"}
Employee3 = {"name": "Varun", "age": 45, "salary": 568687.97, "department": "Management"}
Employee4 = {"name": "Soham", "age": 20, "salary": 324465.12, "department": "HR"}
Employee5 = {"name": "Rahul", "age": 56, "salary": 74343.65, "department": "Engineer"}
Employee6 = {"name": "Ananya", "age": 27, "salary": 542567.83, "department": "Engineer"}
Employee7 = {"name": "Siddharth", "age": 32, "salary": 45657.76, "department": "Management"}

print(average_salary_by_department(Employee1, Employee2, Employee3,Employee4,Employee5,Employee6,Employee7))
highest_salary_department, highest_salary = department_with_highest_salary(Employee1, Employee2, Employee3,Employee4,Employee5,Employee6,Employee7)
print(f"Highest Salary Department: {highest_salary_department}\nHighest Salary: {highest_salary}")
youngest_employee, age, department = youngest_employee_in_department(Employee1, Employee2, Employee3,Employee4,Employee5,Employee6,Employee7)
print(f"The name of the youngest employee is {youngest_employee} and their age is {age} and is from {department} department")
