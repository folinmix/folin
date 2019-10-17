a=[0,2,4,6,8]

while True:
    b=input("”гадай число ('x' - завершить)\n")
    if b=="x":
        break
    else:
        try:
            c=int(b)
            if c in a:
                print ("¬ведЄнное число есть в списке")
            else:
                print ("¬ведЄнного числа в списке нет")
        except ValueError:
            print ("¬ведено не символьное значение числа")
