class Hexagon():
    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.size1=s1
        self.size2=s2
        self.size3=s3
        self.size4=s4
        self.size5=s5
        self.size6=s6

    def perimeter(self):
        return self.size1+self.size2+self.size3+self.size4+self.size5+self.size6


hex1=Hexagon(1,2,3,4,5,6)

a=hex1.perimeter()

print(a)
