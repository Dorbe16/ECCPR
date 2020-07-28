#BINARYSEARCH
import math
n = int(input())
vector = []
for i in range(n):
    vector.append(int(input()))
x = int(input())
vector = sorted(vector)
while len(vector) >= 1:
    print(vector[math.floor(len(vector)/2)])
    mijloc = math.floor(len(vector)/2)
    if x < vector[mijloc]:
        if len(vector[:mijloc]) % 2 != 0:
            vector = vector[:mijloc]
        else:
            vector = vector[:(mijloc + 1)]
    elif x > vector[mijloc]:
        if len(vector[mijloc:]) % 2 == 0:
            vector = vector[(mijloc+1):]
        else:
            vector = vector[(mijloc):]
    else:
        break
    if len(vector) == 1: 
        print(vector[0])
        break
