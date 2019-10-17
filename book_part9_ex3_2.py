import csv

with open("st1.csv","r") as f:
    r=csv.reader(f,delimiter=",")
    for i in r:
        print(",".join(i))
