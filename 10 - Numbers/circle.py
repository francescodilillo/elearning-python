################################################################################
# 
# Author: francescodilillo
# Purpose: Calculate area and circumference of a circle given its radius
# Last Edit Date: 15-03-2020
#
#
################################################################################


import math

radius = float(input("This program will calculate area and circumference of a circle given its radius. Please insert the radius of the circle: "))
area = round(math.pi * (radius ** 2 ),2)
circumference = round(2 * math.pi * radius, 2)

print("Radius: ", radius, "Area: ", area, "Circumference: ", circumference)