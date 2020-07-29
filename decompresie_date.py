#DECOMPRESIE_DATE
n = int(input())
total = []
for j in range(n):
    lst = []
    linie = input().split(",")
    for i in range(len(linie)):
        if '(' not in linie[i] and ')' not in linie[i]:
            lst.append(linie[i])
        elif linie[i][0] == '(':
            lst.extend(tuple([linie[i][1:], (int(linie[i + 1][:-1]) * '0,')[:-1]]))
    total.append(",".join(lst))
for k in total:
    print(k)


















"""
total = []
for j in range(n):
    lst = []
    for i in range(len(linie)):
        if len(linie[i]) == 1:
            lst.append(linie[i])
        elif linie[i][0] == "(":
            lst.extend(tuple([linie[i][1], (int(linie[i+1][0]) * '0,')[:-1]]))
    total.append(",".join(lst))

for i in total:
    print(i)
"""


