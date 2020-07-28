#BUCKETLIST
n = int(input())
dct = {}
valori = list(map(int, input().split()))
for i in valori:
    cifre = 0
    nr = i
    while i > 0:
        i = i//10
        cifre += 1
    if cifre in dct.keys():
        dct.update({cifre: dct[cifre] + 1})
    else:
        dct.update({cifre: 1})
for i in dct.items():
    print(*i)
