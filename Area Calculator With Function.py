import math

# Add your code here

# TODO -> Add welcome function here
def displayWelcome():
  print "Welcome to the Area Calculator!"
  print "-" * 50
# TODO -> Add circle area function here
def calcAreaCircle(radius):
  area = math.pi * radius ** 2
  return area
  
# TODO -> Add circle perimeter function here
def calcPerimeterCircle(radius):
  perimeter = 2 * math.pi * radius
  return perimeter
  
# TODO -> Add square area function here
def calcAreaSquare(side):
  area = side * side
  return area
  
# TODO -> Add Square perimeter function here
def calcPerimeterSquare(side):
  perimeter = side * 4 
  return perimeter
  
# TODO -> Add rectangle area function here
def calcAreaRect(width, height):
  area = width * height
  return area
  
# TODO -> Add rectangle perimeter function here
def calcPerimeterRect(width, height):
  perimeter = 2 * width + 2 * height
  return perimeter
  
# TODO -> Add triangle area function here
def calcAreaTriangle(base, height):
  area = base * height / 2
  return area
  

# =====================================================================

# Main Code - DO NOT EDIT ANYTHING BELOW.  Add your functions above

displayWelcome()


radius = 3.56

area = calcAreaCircle(radius)

perimeter = calcPerimeterCircle(radius)

print('Circle   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


side = 9.23

area = calcAreaSquare(side)

perimeter = calcPerimeterSquare(side)

print('Square   : area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


width = 2.9

height = 14.22

area = calcAreaRect(width, height)

perimeter = calcPerimeterRect(width, height)

print('Rectangle: area = {0:.2f}, perimeter = {1:.2f}'.format(area, perimeter))


base = 7.97

height = 5.31

area = calcAreaTriangle(base, height)

print('Triangle : area = {0:.2f}'.format(area))