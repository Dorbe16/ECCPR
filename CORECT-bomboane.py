n = int(input())
suma = 0 
arome = []
fericire = 0
bani = list(map(int, input().split()))
for i in range(n):
    pret, aroma = input().split()
    pret = int(pret)
    aroma = int(aroma)
    suma += bani[i]
    if suma >= pret:
        suma -= pret
        fericire += aroma
        arome.append(aroma)
    elif suma < pret:
        if not arome:
            fericire -= aroma
        elif arome:
            if aroma >= max(arome):
                fericire -= aroma
print(fericire)
