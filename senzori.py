#SENZORI
n = int(input())
dreapta = []
stanga = []
viteze = []
for i in range(n):
    timp, stare = input().split()
    timp = int(timp)
    stare = int(stare)
    stanga.append(tuple([timp, stare]))
for i in range(n):
    timp, stare = input().split()
    timp = int(timp)
    stare = int(stare)
    dreapta.append(tuple([timp, stare]))
stanga = [i for i in stanga if i[1] == 1]
dreapta = [i for i in dreapta if i[1] == 1]  
for i in range(0, len(stanga), 2):
    timp = dreapta[i][0] - stanga[i][0]
    v = 2 / (timp * 0.01)
    viteze.append(v)
print(int(sum(viteze) / len(viteze)), int(len(stanga)/2))
