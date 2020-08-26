N = int(input())
stoc = list(map(int, input().split()))
n = int(input())
aprov = 0
prost = 0
for _ in range(n):
    cerere = list(map(int, input().split()))
    if cerere.count(cerere[0]) == len(cerere) and cerere[0] == 0:
        aprov += 1
        for i in range(len(stoc)):
            stoc[i] += 10
    else:
        for i in range(len(stoc)):
            if stoc[i] >= cerere[i]:
                stoc[i] -= cerere[i]
            else:
                prost += 1
                break
print(prost)
print(aprov)
