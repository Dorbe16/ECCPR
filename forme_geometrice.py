#FORME_GEOMETRICE
import math
n = int(input())
lst = []
distances = []
for i in range(n):
    coord = input().split()
    lst.append(list(map(float,tuple(coord))))
for i in range(len(lst)-1):
    x1 = lst[i][0]
    x2 = lst[i+1][0]
    y1 = lst[i][1]
    y2 = lst[i+1][1]
    d = math.sqrt((x2-x1) ** 2 + (y2 - y1) ** 2)
    distances.append(d)
x1 = lst[len(lst) - 1][0]
x2 = lst[0][0]
y1 = lst[len(lst) - 1][1]
y2 = lst[0][1]
distances.append(math.sqrt((x2-x1) ** 2 + (y2 - y1) ** 2))
if distances.count(distances[0]) == len(distances):
    print("da")
else:
    print("nu")