import csv

a=[["������� �����","����������","������������� ���������"],["�����","���������","��������"],["���� � ������","� - �����","��������"]]

print(a)

with open("st1.csv","w") as f:
    w=csv.writer(f,delimiter=";")

    w.writerow(["����",
                "���",
                "���"])
    
    w.writerow(["������",
                "����",
                "�����"])

    #for i in range (0,len(a)):
     #   w.writerow(a[i])
