word=input("Загадай слово:\n")
wrong=0
stages=["",
        "________    ",
        "|           ",
        "|      |    ",
        "|      O    ",
        "|     /|\   ",
        "|     / \   ",
        "|           ",
        "|___________"]
rletters=list(word)
board=["_"]*len(word)
win= False
print ("Добро пожаловать на казнь!")
while wrong<len(stages)-1:
    print("\n")
    msg="Ввудите букву:"
    char=input(msg)
    if char in rletters:
        cind=rletters.index(char)
        board[cind]=char
        rletters[cind]="$"
    else:
        wrong+=1
    print((" ".join(board)))
    e=wrong+1
    print("\n".join(stages[0:e]))
    if "_" not in board:
        print ("Вы выиграли! Загаданное слово:")
        print(" ".join(board))
        win=True
        break
if not win:
    print("\n".join(stages[0:wrong]))
    print("Вы проиграли! Загаданное слово:"+word)
