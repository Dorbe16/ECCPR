#CIFRU_SUBSTITUTIE
s = input()
tabel = input().split()
lst = []
nou = ""
for i in tabel:
    lst.append(tuple(i.split(",")))
for i in s:
    bec = 0
    for j in lst:
        if i == j[0]:
            nou += j[1]
            bec = 1
            break
    if not bec:
        nou += i
print(nou)
