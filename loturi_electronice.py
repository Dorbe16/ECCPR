#LOTURI
n = int(input())
utile = 0
loturi = []
lens = []
for i in range(n):
    k = int(input())
    comp = input().split()
    if comp.count("R") >= 1 and comp.count("C") >= 1 and comp.count("T") >=1:
        if comp.count("C") >= comp.count("T") and comp.count("R") >= comp.count("C"):
            utile += 1
    loturi.append(tuple(comp))
    lens.append(k)
print(utile, max(lens))
