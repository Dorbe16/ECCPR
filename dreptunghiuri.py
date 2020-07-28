#DREPTUNGHIURI
n = int(input())
suprafete = []
for i in range(n):
    nume, x1, y1, x2, y2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    suprafete.append(tuple([(x2 - x1) * (y2 - y1), nume, x1, y1, x2, y2]))
print(*sorted(suprafete, reverse = True)[0][1:], end = " ")
print(sorted(suprafete, reverse = True)[0][0])
