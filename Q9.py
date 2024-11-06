def quadrant(x, y):
    if(x == 0 and y == 0):
        print("Origin")
    elif((x > 0 or x < 0) and y == 0):
        print("X-axis")
    elif((y > 0 or y < 0) and x == 0):
        print("Y-axis")
    elif(x > 0 and y > 0):
        print("First quadrant")
    elif(x < 0 and y > 0):
        print("Second quadrant")
    elif(x < 0 and y < 0):
        print("Third quadrant")
    elif(x > 0 and y < 0):
        print("Fourth quadrant")

x = int(input("Enter the x-coordinate: "))
y = int(input("Enter the y-coordinate: "))

quadrant(x, y)