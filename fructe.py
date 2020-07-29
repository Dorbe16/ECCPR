#FRUCTE
import math
n, k, mc, rc, gc, bc = list(map(int, input().split()))
distante = []
for _ in range(n):
    tip, mi, ri, gi, bi = list(map(int, input().split()))
    di = math.sqrt((mc - mi) ** 2 + (rc - ri) ** 2 + (gc - gi) ** 2 + (bc - bi) ** 2)
    distante.append(tuple([di, tip]))
print(sorted(distante)[0][1])