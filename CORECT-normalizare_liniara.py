import collections
width, height = list(map(int, input().split()))
matrice = []
new = []
for _ in range(height):
    linie = list(map(int, input().split()))
    matrice.extend(linie)
gain = 255/(max(matrice) - min(matrice))
for i in matrice:
    new.append(round((i - min(matrice)) * gain))
lista = [i for i in collections.Counter(new).keys() if collections.Counter(new)[i] == max(collections.Counter(new).values())]
print(*sorted(lista))

