print(" Welcome to the Area Calculator! ")
print("Enter 'C' for Circle, 'T' for Triangle or 'R' for Rectangle!")
print("-")*55
name = raw_input("What is the shape?")
if name == "C": 
  radius = float(raw_input("Enter the radius of the circle: "))
  pi = 3.14159
  area = pi * radius * radius
  print(" Area of the Circle is ", area)
elif name == "T": 
    base = float(raw_input("Enter the base of triangle: "))
    height = float(raw_input("Enter the height of triangle: "))
    area = 1/2 * base * height
    print(" Area of Triangle is ", area)
elif name == "R":
    base = float(raw_input("Enter the base of the rectangle: "))
    height = float(raw_input("Enter the height of the  rectangle: "))
    area = base * height
    print(" Area of the Rectangle is ", area)
else:
  print(" >>>You need to enter 'C' for Circle, 'T' for Triangle or 'R' for Rectangle!<<<  ")