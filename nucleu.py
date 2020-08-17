import math
n = int(input())
lovesc = 0
pericol = 0
leptoni = 0
leptoniLovesc = 0
leptoniPericol = 0
hadroni = 0
hadroniLovesc = 0
hadroniPericol = 0
neidentif = 0
neidentifLovesc = 0
neidentifPericol = 0
r = 153
for _ in range(n):
    tip = ""
    particula = list(map(float, input().split()))
    h = (particula[0] + r) * math.tan(particula[2])
    Ec = particula[1] * particula[3] ** 2 // 2
    if h <= r:
        lovesc += 1

        if Ec >= 200000000:
            pericol += 1
    if particula[1] >= 2 and particula[3] <= 10000:
        leptoni += 1
        tip = "lepton"
    elif particula[1] < 2 and particula[3] >= 15000:
        hadroni += 1
        tip = "hadron"
    else:
        neidentif += 1
        tip = "neidentif"
    if tip == "lepton" and h <= r:
        leptoniLovesc += 1
        if Ec >= 200000000:
            leptoniPericol += 1
    if tip == "hadron" and h <= r:
        hadroniLovesc += 1
        if Ec >= 200000000:
            hadroniPericol += 1
    if tip == "neidentif" and h <= r:
        neidentifLovesc += 1
        if Ec >= 200000000:
            neidentifPericol += 1

print(lovesc, pericol)
print(leptoni, hadroni, neidentif)
print(leptoniLovesc, hadroniLovesc, neidentifLovesc)
print(leptoniPericol, hadroniPericol, neidentifPericol)