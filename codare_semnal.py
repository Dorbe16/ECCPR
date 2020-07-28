#CODARE_SEMNAL
m = int(input())
n = int(input())
suma = 0
v1 = []
v2 = []
dct = {}
for i in range(m * n):
    v1.append(int(input()))
for i in v1:
    if i in dct.keys():
        dct.update({i: dct[i] + 1})
    else:
        dct.update({i: 1})
for i in list(dct.items()):
    v2.extend(i)
print(len(v1) - len(v2))
