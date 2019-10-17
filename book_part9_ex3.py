import csv

a=[["Звёздные воины","Терминатор","Искусственный интеллект"],["Дурак","Маатильда","Левиафан"],["Люди в чёрном","Я - робот","Эволюция"]]

print(a)

with open("st1.csv","w") as f:
    w=csv.writer(f,delimiter=";")

    w.writerow(["один",
                "два",
                "три"])
    
    w.writerow(["четыре",
                "пять",
                "шесть"])

    #for i in range (0,len(a)):
     #   w.writerow(a[i])
