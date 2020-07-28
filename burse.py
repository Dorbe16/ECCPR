#BURSE
nr = 0
bursieri = []
m, n, p = input().split()
m = int(m)
n = int(n)
p = int(p)
for i in range(m):
    nume = input()
    note = list(map(int, input().split()))
    if sum(note) / len(note) >= 8 and all([nota >= 5 for nota in note]):
        nr += 1
    bursieri.append(tuple([float(format(sum(note) / len(note), '.2f')), nume]))
bursieri = sorted(bursieri, reverse = True)
if nr - 1 <= p:
    print(nr - 1)
else:
    print(p)
print(bursieri[0][1], format(bursieri[0][0], '.2f'))
