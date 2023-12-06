# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

from math import pi

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None and diameter is not None:
            raise ValueError("Specify either radius or diameter, not both.")
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Specify either radius or diameter.")
    
    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return pi * self.radius ** 2

    def __str__(self):
        return f"Circle with radius {self.radius}"

    def __add__(self, other):
        return Circle(radius=self.radius + other.radius)

    def __lt__(self, other):
        return self.radius < other.radius

    def __eq__(self, other):
        return self.radius == other.radius

circle1 = Circle(radius=3)
circle2 = Circle(diameter=4)
print(circle1.area)  
print(circle2.diameter)  

circle3 = circle1 + circle2
print(circle3.radius) 

circles = [Circle(radius=15), Circle(radius=22), Circle(radius=38)]
sorted_circles = sorted(circles)

for circle in sorted_circles:
    print(circle)

import turtle

def draw_circle(circle):
    turtle.penup()
    turtle.goto(0, -circle.radius)
    turtle.pendown()
    turtle.circle(circle.radius)

for circle in sorted_circles:
    draw_circle(circle)

turtle.done()