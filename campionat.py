def key(elem):
    return elem[1]
k = int(input())
n = int(input())
meciuri = []
goluriDate = {}
goluriPrimite = {}
punctaje = {}
for i in range(n):
    meci = input().split()
    echipa1 = meci[0]
    scor1 = int(meci[1])
    scor2 = int(meci[3])
    echipa2 = meci[4]
    if echipa1 not in punctaje.keys():
        punctaje.update({echipa1: 0})
    if echipa2 not in punctaje.keys():
        punctaje.update({echipa2: 0})
    if scor1 == scor2:
        punctaje.update({echipa1: punctaje[echipa1] + 1})
        punctaje.update({echipa2: punctaje[echipa2] + 1})
    elif scor1 > scor2:
            punctaje.update({echipa1: punctaje[echipa1] + 3})
    elif scor2 > scor1:
            punctaje.update({echipa2: punctaje[echipa2] + 3})
    if echipa1 not in goluriDate.keys():
        goluriDate.update({echipa1: scor1})
    else:
        goluriDate.update({echipa1: goluriDate[echipa1] + scor1})
    if echipa2 not in goluriDate.keys():
        goluriDate.update({echipa2: scor2})
    else:
        goluriDate.update({echipa2: goluriDate[echipa2] + scor2})
    if echipa1 not in goluriPrimite.keys():
        goluriPrimite.update({echipa1: scor2})
    else:
        goluriPrimite.update({echipa1: goluriPrimite[echipa1] + scor2})
    if echipa2 not in goluriPrimite.keys():
        goluriPrimite.update({echipa2: scor1})
    else:
        goluriPrimite.update({echipa2: goluriPrimite[echipa2] + scor1})

for i in punctaje.keys():
    meciuri.append(tuple([i, punctaje[i], goluriDate[i], goluriPrimite[i]]))
meciuri = sorted(meciuri, key = key, reverse = True)
for i in meciuri:
    print(*i)
