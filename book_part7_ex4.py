a=[0,2,4,6,8]

while True:
    b=input("������ ����� ('x' - ���������)\n")
    if b=="x":
        break
    else:
        try:
            c=int(b)
            if c in a:
                print ("�������� ����� ���� � ������")
            else:
                print ("��������� ����� � ������ ���")
        except ValueError:
            print ("������� �� ���������� �������� �����")
