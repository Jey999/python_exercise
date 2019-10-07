# This is your exercise file.
# Here you'll find tips and you'll edit code.
# To run the tests run: pytest specs_101.py
import math
# Finish the  hello_human function
def hello_human(name):
    return (f"Hello {name}, you are a humman")

# Finish the area of square function
def area_square(length):
    area= length * length
    return area




# Define a function that take in 2 arguments to calculate the area of a triangle

def area_triangle(base,height):
    areaoftriangle= (base*height)/2
    return areaoftriangle

#define are of circle

def area_of_circle(radius):
    return round(math.pi*radius**2,2)

#define