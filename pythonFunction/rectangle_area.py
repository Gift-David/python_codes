# A function to calculate the area of a rectangle

print("This programme calculates the area of a rectangle")
length = float(input("Enter the Length: "))
width = float(input("Enter the width: "))

def area(length, width):
    area = length * width
    return area

print(area(length, width))
