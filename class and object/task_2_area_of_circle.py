'''
 Create a circle class that will take the value of a radius and 
 return the area of the circle
'''
import math as m

class Circle():
    def __init__(self, radius):
        self.radius = radius

    def area_of_circle(self):
        area = m.pi * ((self.radius) ** 2)
        return area
        
my_circ = Circle(5)
result = my_circ.area_of_circle()
print(result)