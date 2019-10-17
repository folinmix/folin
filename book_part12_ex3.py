import math

class Triangle():
    def __init__(self,s1,s2,s3):
        self.size1=float(s1)
        self.size2=float(s2)
        self.size3=float(s3)

    def area(self):
        p=(self.size1+self.size2+self.size3)/2
        s=p*(p-self.size1)*(p-self.size2)*(p-self.size3)
        return math.sqrt(s)

tri1=Triangle(1,1,1)

a=tri1.area()

print(a)
