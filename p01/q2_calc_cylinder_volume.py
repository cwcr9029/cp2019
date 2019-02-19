import math

radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
area = math.pi * radius ** 2
volume = area * height
print("Base area of the cylinder is " + str(area))
print("Base area of the cylinder is " + str(volume))