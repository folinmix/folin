class Shape():
    def __init__(self,s1,s2):
        self.size1=s1
        self.size2=s2

    def whoami(self):
        print("� - ������")

class Rectangle(Shape):
    def perimeter(self):
        return self.size1*2+self.size2*2

    def whoami(self):
        print("� - ��������������")

class Square(Shape):
    def perimeter(self):
        return self.size1*4
    
    def whoami(self):
        print("� - �������")

        
re1=Rectangle(1,2)
sq1=Square(1,1)

a=[re1,sq1]

for i in a:
    print(i.perimeter())
    i.whoami()
