#ARANJAMENTE
import math
k,M = input().split()
k = int(k)
M = int(M)
aranjamente = []
for i in range(k,M//2):
    m = math.factorial(i) / math.factorial(i-k)
    if m <= M:
        aranjamente.append(i)
    else:
        break
if aranjamente != []:
    print(max(aranjamente))
else:
    print(0)