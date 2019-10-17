class Horse():
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner

class Person():
    def __init__(self,name):
        self.name=name


per=Person("Бобо")
hor=Horse("Микки","Пржевальского",per)

print(hor.owner.name)
