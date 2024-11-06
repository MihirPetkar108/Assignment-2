def triangleType(side1, side2, side3):
    if(side1 == side2 == side3):
        print("The triangle is an Equilateral triangle!")
    elif((side1 == side2) or (side1 == side3) or (side2 == side3)):
        print("The triangle is an Isosceles triangle!")
    elif(side1 != side2 != side3):
        print("The triangle is an Scalene triangle!")

def area_of_triangle(side1,side2,side3):
    s = (side1 + side2 + side3)/2 # Semi-Perimeter
    Area = round((s*(s-side1)*(s-side2)*(s-side3))**0.5,2)
    print(f"Area of the triangle is {Area}")

side1 = int(input("Enter length 1: "))
side2 = int(input("Enter length 2: "))
side3 = int(input("Enter length 3: "))

triangleType(side1, side2, side3)
area_of_triangle(side1,side2,side3)