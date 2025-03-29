def quadrant_finder(x, y):
    if x > 0 and y > 0:
        return "1st Quadrant"
    elif x < 0 and y > 0:
        return "2nd Quadrant"
    elif x < 0 and y < 0:
        return "3rd Quadrant"
    elif x > 0 and y < 0:
        return "4th Quadrant "
    elif x == 0 and y != 0:
        return "On the Y-axis"
    elif y == 0 and x != 0:
        return "On the X-axis"
    else:
        return "Origin"

x = float(input("Enter the  x-coordinate: "))
y = float(input("Enter the y-coordinate: "))
print("The point is in:", quadrant_finder(x, y))


