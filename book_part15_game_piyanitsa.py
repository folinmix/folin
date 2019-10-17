from random import shuffle

class Card:
    masti=["пика","черва","буба","креста"]
    karti=[None,None,"два","три","четыре","пять","шесть","семь","восемь","девять","десять","валет","дама","король","туз"]

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
        name1=input("Имя первого игрока:\n")
        name2=input("Имя второго игрока:\n")
        self.deck=Deck()
        self.p1=Player(name1)
        self.p2=Player(name2)

    def wins(self,winner):
        w="{0} забирает карты"
        w=w.format(winner)
        print(w)

    def draw(self,p1n,p1c,p2n,p2c):
        d="{0} кладёт {1}, а {2} кладёт {3}".format(p1n,p1c,p2n,p2c)
        #d=d.
        print(d)

    def play_game(self):
        cards=self.deck.cards
        print("Начали")
        ip=1
        while len(cards)>=2:
            #m="Нажмите Х для выхода. Любая другая клавиша - продолжение игры.\n"
            #responce=input(m)
            #if responce=='X' or responce=='x':
            #    break
            print("--------------Раунд {0}--------------".format(ip))
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
        print("Игра окончена. {0} победил!".format(win))

    def winner(self,p1,p2):
        if p1.wins>p2.wins:
            return p1.name
        if p1.wins<p2.wins:
            return p2.name
        return "Ничья"

game=Game()
game.play_game()




