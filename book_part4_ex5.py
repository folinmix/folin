a='два'

try:
    b=float(a)
    print(b)
except ValueError:
    print ("Введите число символом")
