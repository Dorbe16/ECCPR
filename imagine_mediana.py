#IMAGINE_MEDIANA
m = int(input())
n = int(input())
matrice = [list(map(int, [char for char in '0' * (n+2)]))]
af = []
for i in range(m):
    linie = []
    linie.append(0)
    for j in range(n):
        elem = int(input())
        linie.append(elem)
    linie.append(0)
    matrice.append(linie)
matrice.append(list(map(int, [char for char in '0' * (n+2)])))
print(matrice)
for i in range(1,m + 1):
    linie = []
    for j in range(1, n + 1):
        median = sorted([matrice[i-1][j], matrice[i][j-1], matrice[i][j], matrice[i][j+1], matrice[i+1][j]])
        linie.append(median[len(median)//2])
    af.append(linie)
for _ in af:
    for x in _:
        print(x)