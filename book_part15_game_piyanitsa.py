from random import shuffle

class Card:
    masti=["����","�����","����","������"]
    karti=[None,None,"���","���","������","����","�����","����","������","������","������","�����","����","������","���"]

    def __init__ (self,k,m):
        self.karta=k
        self.mast=m

    def __lt__ (self,c2):
        if self.karta<c2.karta:
            return True
        if self.karta==c2.karta:
            if self.mast<c2.mast:
                return True
            else:
                return False
        return False

    def __gt__ (self,c2):
        if self.karta>c2.karta:
            return True
        if self.karta==c2.karta:
            if self.mast>c2.mast:
                return True
            else:
                return False
        return False

    def __repr__ (self):
        karta=self.karti[self.karta]+" "+self.masti[self.mast]
        return karta

class Deck:
    def __init__ (self):
        self.cards=[]
        for i in range (2,15):
            for j in range (4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards)==0:
            return
        return self.cards.pop()

class Player:
    def __init__(self,name):
        self.wins=0
        self.card=None
        self.name=name

class Game:
    def __init__(self):
        name1=input("��� ������� ������:\n")
        name2=input("��� ������� ������:\n")
        self.deck=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)

    def wins(self,winner):
        w="{0} �������� �����"
        w=w.format(winner)
        print(w)

    def draw(self,p1n,p1c,p2n,p2c):
        d="{0} ����� {1}, � {2} ����� {3}".format(p1n,p1c,p2n,p2c)
        #d=d.
        print(d)

    def play_game(self):
        cards=self.deck.cards
        print("������")
        ip=1
        while len(cards)>=2:
            #m="������� � ��� ������. ����� ������ ������� - ����������� ����.\n"
            #responce=input(m)
            #if responce=='X' or responce=='x':
            #    break
            print("--------------����� {0}--------------".format(ip))
            p1c=self.deck.rm_card()
            p2c=self.deck.rm_card()
            p1n=self.p1.name
            p2n=self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c>p2c:
                self.p1.wins+=1
                self.wins(self.p1.name)
            else:
                self.p2.wins+=1
                self.wins(self.p2.name)
            ip+=1
        win=self.winner(self.p1,self.p2)
        print("���� ��������. {0} �������!".format(win))

    def winner(self,p1,p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins<p2.wins:
            return p2.name
        return "�����"

game=Game()
game.play_game()




