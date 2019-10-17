class Rectangle():
    def __init__(self,s1,s2):
        self.size1=s1
        self.size2=s2
        
    def perimeter(self):
        return self.size1*2+self.size2*2

class Square():
    def __init__(self,s1):
        self.size=s1
        
    def perimeter(self):
        return self.size*4
        
re1=Rectangle(1,2)
sq1=Square(2)

a=[re1,sq1]

for i in a:
    print(i.perimeter())


