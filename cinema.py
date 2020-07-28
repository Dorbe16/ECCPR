#CINEMATOGRAF
from datetime import datetime as dt
time = input()
fmt = '%H:%M'
filme = []
minim = 9999999999999999
n = int(input())
for i in range(n):
    ora, pret, nume = input().split()
    delta = (dt.strptime(ora, fmt) - dt.strptime(time, fmt)).total_seconds()
    if delta <= minim and delta > 0:
        minim = delta
        filme.append(tuple([delta, pret, nume]))
print(sorted(filme)[0][2])
