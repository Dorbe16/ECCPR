#CONTROLOR_TRAFIC
n = int(input())
numere = list(map(int, input().split()))
suma = 0
for i in range(1, n + 1): 
	if i not in numere: suma += i
print(suma)
