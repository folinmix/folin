class Horse():
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner

class Person():
    def __init__(self,name):
        self.name=name


per=Person("����")
hor=Horse("�����","�������������",per)

print(hor.owner.name)
