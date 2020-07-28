#BIBLIOTECA
D, k = list(map(int, input().split()))
dct = {}
for i in range(k):
    n, p = list(map(int, input().split()))
    dct.update({p: n})
while dct != {}:  
    grosime = 0
    raft = []
    while grosime <= D:
        bune = []
        for i in dct.keys():
            if dct[i] > 0 and i <= D - grosime:
                bune.append(i)
        if bune != []:
            dct.update({max(bune): (dct[max(bune)] - 1)})
            grosime += max(bune)
            raft.append(max(bune))
        else: break
    if raft != []: print(*raft)
    else: break
