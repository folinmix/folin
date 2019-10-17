class perem():
    def __init__(self):
        self.name='dodo'

def che(x,y):
    if x is y:
        return True
    else:
        return False

x=perem()
y=x

a=che(x,y)
print(a)
print("------------")

x=perem()
y=perem()

a=che(x,y)
print(a)

