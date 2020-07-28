#CODARE_DATE
sume = []
n = int(input())
for _ in range(n):
    nr = input().split(" ")
    for i in range(0,len(nr)-1,2):
        tmp = nr[i]
        nr[i] = nr[i+1]
        nr[i+1] = tmp
    nr[0] = int(nr[0])
    for i in range(1,len(nr)):
        nr[i] = int(nr[i])
        nr[i] = nr[i] % 2
    sume.append(sum(nr))
print(max(sume))
