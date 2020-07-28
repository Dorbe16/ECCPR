#CRIPTANALIZA
n, k = map(int, input().split())
val = [*map(int, input().split())]
prime = []
for i in val:
    bec = 0
    for j in range(2, i//2):
        if i % j == 0:
            bec = 1
            break
    if not bec and i >= k:
        prime.append(i)
if prime != []: print(min(prime))
else: print(-1)