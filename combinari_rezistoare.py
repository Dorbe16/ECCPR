#COMBINARI_REZISTOARE
import math
n, M = list(map(int, input().split()))
nr = []
for k in range(n):
    m = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    if M <= m:
        nr.append(k)
if nr != []: print(min(nr))
else: print(0)
