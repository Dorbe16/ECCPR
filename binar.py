#BINAR
n = int(input())
binare = []
maxim = 0
nou = []
for i in range(n):
    resturi = ""
    numar = int(input())
    nr = numar
    while nr > 0:
        resturi += str(nr % 2)
        nr = nr // 2
    elem = "".join(list(reversed(resturi)))
    binare.append(tuple([elem.zfill(8), numar]))  
for i in binare:
    if i[0].count('0') >= maxim:
        maxim = i[0].count('0')
        nou.append(tuple([maxim, i[1]]))
for i in nou:
    if i[0] == maxim:
        print(i[1])
