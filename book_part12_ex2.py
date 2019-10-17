import math

class Circle():
    def __init__(self,r):
        self.radius=r

    def area(self):
        return math.pi*(self.radius**2)

cir1=Circle(5)
a=cir1.area()
print(a)
