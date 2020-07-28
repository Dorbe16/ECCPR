#STARWARS
ala, bala = list(map(int, input().split()))
n = int(input())
nr = 0
for i in range(n):
    ps = ala
    pf = bala
    s, f = list(map(int, input().split()))
    while ps >= 0 and s >= 0:
        ps -= f
        s -= pf
        if s < 0 and ps >= 0:
            nr += 1
print(nr)
